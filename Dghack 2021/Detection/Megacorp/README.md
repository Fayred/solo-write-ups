# Megacorp

## Megacorp 1

![](https://i.imgur.com/pnsTDHh.png)

Dans cette suite de challenges, nous devons identifier l'intrusion.

Dans "Megacorp 1", nous devons trouver le sha256 du fichier ayant initié la compromission dans le domaine sur : [Kibana](http://kibana-tuazhu.inst.malicecyber.com/).

Une fois authentifier, on va dans le menu à gauche et on clique sur ``Discover``.

Ensuite on affiche les logs dans l'année, et on voit qu'il y en a 3030 :

![](https://i.imgur.com/TpUBupY.png)

Il faut donc utiliser les filtres pour afficher le checksum des fichiers, l'emplacements et le noms et afficher seulement les lignes contenant le champ `winlog.event_data.Hash`.

Pour ce faire on va dans la barre de recherche à gauche et selectionner les champs : `winlog.event_data.Hash` et `winlog.event_data.TargetFilename`.

Après on cherche dans la barre supérieur `winlog.event_data.Hash : *` afin d'afficher seulement les lignes contenant le champ `winlog.event_data.Hash : * ` :

 ![](https://i.imgur.com/PiNUNFt.png)

Une fois cela fait nous avons 6 résultats dont le fichier initiant l'attaque, qui est `C:\Users\uri.cato\Downloads\cv_stagiaire.docm` avec un hash sha256 à : `3F0A801DEBE411DBCA3B572796116B56B527F85823FA84B03223CB68161D07BF`.

On peut donc valider avec le flag : `DGA{3F0A801DEBE411DBCA3B572796116B56B527F85823FA84B03223CB68161D07BF}`.
