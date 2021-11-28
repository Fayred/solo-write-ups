# Megacorp

## Megacorp 1 - 50 points

![](https://i.imgur.com/pnsTDHh.png)

Dans cette suite de challenges, nous devons identifier l'intrusion.

Dans "Megacorp 1", nous devons trouver le sha256 du fichier ayant initié la compromission dans le domaine sur : [Kibana](http://kibana-tuazhu.inst.malicecyber.com/).

Une fois authentifié, on va dans le menu à gauche et on clique sur ``Discover``.

Ensuite on affiche les logs dans l'année, et on voit qu'il y en a 3030 :

![](https://i.imgur.com/TpUBupY.png)

Il faut donc utiliser les filtres pour afficher le checksum des fichiers, l'emplacements et le noms et afficher seulement les lignes contenant le champ `winlog.event_data.Hash`.

Pour ce faire on va dans la barre de recherche à gauche et sélectionne les champs : `winlog.event_data.Hash` et `winlog.event_data.TargetFilename`.

Après on cherche dans la barre supérieur `winlog.event_data.Hash : *` afin d'afficher seulement les lignes contenant le champ `winlog.event_data.Hash` :

 ![](https://i.imgur.com/PiNUNFt.png)

Une fois cela fait nous avons 6 résultats dont le fichier initiant l'attaque, qui est `C:\Users\uri.cato\Downloads\cv_stagiaire.docm` avec un hash sha256 à : `3F0A801DEBE411DBCA3B572796116B56B527F85823FA84B03223CB68161D07BF`.

On peut donc valider avec le flag : `DGA{3F0A801DEBE411DBCA3B572796116B56B527F85823FA84B03223CB68161D07BF}`.

## Megacorp 2 - 150 points

![](https://i.imgur.com/2bihXPl.png)

Dans "Megacorp 2", nous devons retrouver le nom du service ayant permis d'effectuer un pivot vers la machine `DK2021002`.

On peut rapidement trouver le service en question en sélectionnant les champs `winlog.event_data.ServiceName` et `host.hostname` à gauche.

Puis en cherchant dans la barre du haut : `host.hostname : DK2021002 and winlog.event_data.ServiceName: *` :

![](https://i.imgur.com/R4PHMWr.png)

On valider le challenge avec le flag : `DGA{tAdOaSoAfpmBCIRD}`

## Megacorp 3 - 50 points

![](https://i.imgur.com/a0vUWL2.png)

Pour "Megacorp 3", nous devons trouver le process GUID du programme ayant été utilisé pour la génération du golden ticket.

On va donc commencer à selectionner les champs `process.name`,  `message` et `process.hash.sha256` à gauche.

Ensuite on cherche dans la barre en haut : `process.name : *` .

On a 322 résultats, on regarde un peu ce que l'on à jusqu'à tomber sur un processus au nom de `mimikatz.exe` :

![](https://i.imgur.com/QDDdJBK.png)

> Mimikatz est un outil de pointe de post-exploitation qui est capable de décharger les mots de passe de la mémoire, mais aussi les hash, les codes PIN et les tickets pour le protocole d'identification réseau Kerberos.

On peut ensuite vérifier la signature en sha256 du fichier sur virustotal pour vérifier que ce soit bien le logiciel `Mimikatz` en question :

![](https://i.imgur.com/cUDgEt3.png)

C'est bien le logiciel en question, il suffit donc de récupérer le process guid affiché dans le champ `message` et de valider le challenge avec.

Flag : `DGA{0FEEC322-9042-6169-8900-000000001D00}`.
