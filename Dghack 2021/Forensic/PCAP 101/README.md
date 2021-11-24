# PCAP 101 - 50 points

![](https://i.imgur.com/hKKPgcd.png)

Pour ce challenge en forensic, on nous donne un fichier pcap à analyser.

On ouvre donc le fichier avec wireshark et on analyse les paquets, plus particulièrement les requêtes http.

On liste les objets http et on peut voir certains noms de fichiers intéressant, dont un ce nommant  `zippassword`:

![](https://i.imgur.com/UbCur9k.png)

On enregistre donc ce fichier et on commence à analyser son contenu :

```
$ cat zippassword 
VGpaU0lWSllaRUZ2VkdwTktqTnhDZz09ClBLAwQKAAkIAAAnazFThNkEHzoAAAAuAAAABgAcAOaX
l+W5n1VUCQADGntEYRp7RGF1eAsAAQToAwAABOkDAADNTNMdVs2aAiv/QpGicu9gTusiwYydh7P8
PAIintAsmf9naL7Zl3FVktVleWKCUUQnG9TVKXa3aZl/UEsHCITZBB86AAAALgAAAFBLAQIeAwoA
CQgAACdrMVOE2QQfOgAAAC4AAAAGABgAAAAAAAEAAACkgQAAAADml5fluZ9VVAUAAxp7RGF1eAsA
AQToAwAABOkDAABQSwUGAAAAAAEAAQBMAAAAigAAAAAA

```

Le contenue est en base64, on le décode et on redirige le résultat vers un fichier :

```
$ base64 -d zippassword > zipPass
```

Maintenant voyant ce que nous avons :

```
$ base64 -d zippassword > zipPass

$ file zipPass 
zipPass: data

$ hd zipPass 
00000000  54 6a 5a 53 49 56 4a 59  5a 45 46 76 56 47 70 4e  |TjZSIVJYZEFvVGpN|
00000010  4b 6a 4e 78 43 67 3d 3d  0a 50 4b 03 04 0a 00 09  |KjNxCg==.PK.....|
00000020  08 00 00 27 6b 31 53 84  d9 04 1f 3a 00 00 00 2e  |...'k1S....:....|
00000030  00 00 00 06 00 1c 00 e6  97 97 e5 b9 9f 55 54 09  |.............UT.|
00000040  00 03 1a 7b 44 61 1a 7b  44 61 75 78 0b 00 01 04  |...{Da.{Daux....|
00000050  e8 03 00 00 04 e9 03 00  00 cd 4c d3 1d 56 cd 9a  |..........L..V..|
00000060  02 2b ff 42 91 a2 72 ef  60 4e eb 22 c1 8c 9d 87  |.+.B..r.`N."....|
00000070  b3 fc 3c 02 22 9e d0 2c  99 ff 67 68 be d9 97 71  |..<."..,..gh...q|
00000080  55 92 d5 65 79 62 82 51  44 27 1b d4 d5 29 76 b7  |U..eyb.QD'...)v.|
00000090  69 99 7f 50 4b 07 08 84  d9 04 1f 3a 00 00 00 2e  |i..PK......:....|
000000a0  00 00 00 50 4b 01 02 1e  03 0a 00 09 08 00 00 27  |...PK..........'|
000000b0  6b 31 53 84 d9 04 1f 3a  00 00 00 2e 00 00 00 06  |k1S....:........|
000000c0  00 18 00 00 00 00 00 01  00 00 00 a4 81 00 00 00  |................|
000000d0  00 e6 97 97 e5 b9 9f 55  54 05 00 03 1a 7b 44 61  |.......UT....{Da|
000000e0  75 78 0b 00 01 04 e8 03  00 00 04 e9 03 00 00 50  |ux.............P|
000000f0  4b 05 06 00 00 00 00 01  00 01 00 4c 00 00 00 8a  |K..........L....|
00000100  00 00 00 00 00                                    |.....|
00000105

```

On voit deux choses :

- Une chaine semblant être encodé en base64 est présent au début du fichier.

- Le fichier semble être un fichier zip, on peut le deviner grâce au nom ``zippassword`` et grâce aux lettres ``PK`` présent dans le header des fichiers zip. 

Pour commencer on décode la chaine en base64 :

```
$ echo -n "TjZSIVJYZEFvVGpNKjNxCg=="|base64 -d
N6R!RXdAoTjM*3q
```

On récupère la chaine de caractère ``N6R!RXdAoTjM*3q``, on ne sait pour le moment pas à quoi elle sert, on la met donc de côté.

Ensuite on va enlever la chaine en base64 au début du fichier avec un éditeur hexadécimal :

![](https://i.imgur.com/kKevsEi.png)

Une fois cela fait on ce retrouve bien avec un fichier zip :

```
$ file zipPass 
zipPass: Zip archive data, at least v1.0 to extract
```

On le dézippe donc le fichier, cependant on nous demande d'entrer un mot de passe pour extraire le contenu.

Il suffit de rentré la chaine de caractères trouvé précédement (``N6R!RXdAoTjM*3q``), qui correspond au mot de passe à rentrer :

```
$ unzip zipPass
Archive:  zipPass
[zipPass] 旗幟 password: 
 extracting: 旗幟      
            
$ cat '旗幟'
DGA{582158848efebaee4d501e98768b012f104cf03c}

```

On a donc le flag : ``DGA{582158848efebaee4d501e98768b012f104cf03c}``.


