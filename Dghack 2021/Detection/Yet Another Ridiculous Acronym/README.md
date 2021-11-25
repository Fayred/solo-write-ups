# Yet Another Ridiculous Acronym - 100pts

<img src="https://i.imgur.com/hYAfA9u.png" title="" alt="" width="727">

Dans ce challenge, on nous donne deux fichiers. On nous donne une image et un fichier compressé contenant 1000 binaires.

Notre but est de trouver le binaire correspondant à celui analysé avec radare2 sur la capture d'écran `r2.png` :

![](https://i.imgur.com/l5ZYDRJ.png)

D'après ces informations, le binaire analysé sur la capture n'a pas de protection NX.

Ensuite les 32 (0x20) octets du binaire à l'adresse `0x0040404f` ont un checksum md5 à `f3ea40bcc61066261ea3a018560434e2`.

Pour finir à une certaine adresse quelque chose est XOR avec les octets d'une certaine adresse.

On doit donc réaliser un programme permettant de trouver le binaire n'ayant pas de protection NX, un checksum md5 à l'adresse `0x0040404f` de `f3ea40bcc61066261ea3a018560434e2` et des valeurs égales à ``0x63 0x69 0x78 0x69 0x78 0x69 0x28`` à la suite XOR avec une même clé.

Le programme de solve en question :

```python
import hashlib
from pwn import *

for x in range(1,912):
    NX = ELF("samples/sample"+str(x), checksec=False).nx
    if NX == False:
	    f_bin = open("samples/sample"+str(x), "rb").read()
	    hex_content = f_bin.hex()
# pour md5_block, j'ai cherché les valeurs des octets correspondant à l'adresse
# 0x0040404f avec radare2 et j'ai cherché dans un lecteur hexa la position 
# des valeurs en octets trouvé précédement dans r2 (position : 12367)
# et comme hex_content est en hexa (str) il suffit de faire x2
	    md5_block = hashlib.md5(bytes.fromhex(hex_content[24734:24734+0x20*2])).hexdigest()
	    if md5_block == "f3ea40bcc61066261ea3a018560434e2":
		    hex_result = [0x63, 0x69, 0x78, 0x69, 0x63, 0x69, 0x78, 0x69, 0x28]
		    i = 0
		    for key in range(1, 255):
		        for character in f_bin:
		            xor = character^key
		            if i == len(hex_result)-1:
		                print(f"KEY : {key} | FILE : sample{x}")
		                i=0
		            if xor == hex_result[i]:
		                i+=1
		            else:
		                i = 0
		        i = 0
```

Résultat :

```
$ python3 solve.py 
KEY : 34 | FILE : sample256
```

Il suffit maintenant d'éxecuter le binaire en question pour obtenir le flag :

```
$ ./sample256
DGA{ca17ba40c5ae2eb3}
```

Le Flag permettant de valider est donc : ``DGA{ca17ba40c5ae2eb3}``.
