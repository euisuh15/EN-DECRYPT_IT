from Crypto.Cipher import AES
from Crypto import Random

import os, sys

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size) #initialization vector

#To send to the opponent
print("\nKEY: ", key)
print("IV: ", iv,"\n")

inFiles = os.listdir("1ORIGINAL")

for file in inFiles:
	input_file = open("1ORIGINAL/"+file, "rb")
	input_data = input_file.read()
	input_file.close()

	cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
	enc_data = cfb_cipher.encrypt(input_data)

	#remove extension
	mfile = file[:-4]
	extension = file[-4:]

	enc_file = open("2ENCRYPTED/"+mfile+".enc", "wb")
	enc_file.write(enc_data)
	enc_file.close()

	enc_file2 = open("2ENCRYPTED/"+mfile+".enc", "rb")
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	output_file = open("3DECRYPTED/"+mfile+extension, "wb")
	output_file.write(plain_data)
	output_file.close()



