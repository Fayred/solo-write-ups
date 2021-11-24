import hashlib
from pwn import *

for x in range(1,912):
    NX = ELF("samples/sample"+str(x), checksec=False).nx
    if NX == False:
	    f_bin = open("samples/sample"+str(x), "rb").read()
	    hex_content = f_bin.hex()
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
