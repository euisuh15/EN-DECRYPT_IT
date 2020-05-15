from Crypto.Cipher import AES
from Crypto import Random

import os, sys

#KEYIV used for encrypting KEYIV
key0 = b'\xbd4k/\xac\xf2\xfc\xff\xa6\x03\x7f\x10W\x83e\xba' 
iv0 = b'\xeb\x0f1\x1c\xd8\xa5\x8d\xf5d\x97\x9aJ\xd8\xb9_\xeb' 

#Decrypting KEYIV
print ("Decrypting KEYIV")
enc_file1 = open("KEYIV.enc", "rb")
enc_data1 = enc_file1.read()
enc_file1.close()

cfb_decipher = AES.new(key0, AES.MODE_CFB, iv0)
plain_data = cfb_decipher.decrypt(enc_data1)

output_file = open("KEYIV.txt", "wb")
output_file.write(plain_data)
output_file.close()
print ("Decrypting Completed\n")

#Retrieving KEY and IV used for decryption
print ("Retrieving KEYIV")
keyiv = open ("KEYIV.txt", 'r')
ki = keyiv.readlines()
keyiv.close()
print ("Retrieving completed\n")


#Modifying decrypt algorithm according to the keyiv
print ("Retrieving Decrypt to modify according to KEYIV")
f = open("Decrypt03.py",'r')
content = f.readlines()
f.close()
print ("Retrieving completed\n")

print ("Modifying Decrypt according to KEYIV")
content[5] = ki[0]
content[6] = ki[1]
newcontent = "".join(content)

f = open("Decrypt03.py", 'w')
f.write(newcontent)
f.close()
print ("Modifying completed\n\n")

#Decrypting Completed
os.system ('python Decrypt03.py')


#Modifying decrypt back to initial stage
f = open("Decrypt03.py",'r')
content = f.readlines()
f.close()
content[5] = "key = \n"
content[6] = "iv = \n"
newcontent = "".join(content)

f = open("Decrypt03.py", 'w')
f.write(newcontent)
f.close()

