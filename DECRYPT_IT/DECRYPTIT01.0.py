from Crypto.Cipher import AES
from Crypto import Random

import os, sys

key = 
iv = 

print ("Retrieving files in 2ENCRYPTED")
inFiles = os.listdir("2ENCRYPTED")
print ("Retrieving completed")
print ("Beginning Decryption\n")

for file in inFiles:
	print ("Decrypting", file)

	enc_file2 = open("2ENCRYPTED/"+file, "rb")
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	output_file = open("3DECRYPTED/"+file[:-4], "wb")
	output_file.write(plain_data)
	output_file.close()
	print ("Completed decrypting", file, "\n")

print ("Decrypting Completed\n")
