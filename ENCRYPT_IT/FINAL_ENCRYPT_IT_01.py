from Crypto.Cipher import AES
from Crypto import Random

import os, sys

#KEYIV used for encrypting KEYIV
key0 =
iv0 =

#KEYIV used for encrypting data
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size) #initialization vector

# print ("\nKEY:", key)
# print ("IV:", iv, "\n")

try:
	os.system('mkdir 1ORIGINAL')
except:
	pass

print ("The program allows you to encrypt files")
print ("Please put the files you want to encrypt in \'1ORIGINAL\'")
temp = input ("Press \'Enter\' key to continue...")

print ("Retrieving files in 1ORIGINAL\n")

try:
	inFiles = os.listdir("1ORIGINAL")
except:
	raise Exception('Directory \'1ORIGINAL\' does not exist in the current directory')

print ("Retrieving completed")

print ("Beginning Encryption\n")

for file in inFiles:
	print ("Encrypting", file)
	input_file = open("1ORIGINAL/"+file, "rb")
	input_data = input_file.read()
	input_file.close()

	cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
	enc_data = cfb_cipher.encrypt(input_data)

	try:
		os.system('mkdir 2ENCRYPTED')
	except:
		pass

	enc_file = open("2ENCRYPTED/"+file+".enc", "wb")
	enc_file.write(enc_data)
	enc_file.close()
	print ("Encrypting Completed")

	print ("Decrypting", file)
	enc_file2 = open("2ENCRYPTED/"+file+".enc", "rb")
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	try:
		os.system('mkdir 3DECRYPTED')
	except:
		pass

	output_file = open("3DECRYPTED/"+file, "wb")
	output_file.write(plain_data)
	output_file.close()
	print ("Completed decrypting", file, "\n")

print ("Encryption successful\n")

# Creating txt with key and iv used for encryption
print ("Generating KEYIV for the recipient")
f = open("KEYIV.key", "w+")
f.write("key = %s \n" %key)
f.write("iv = %s \n" %iv)
f.close()

input_file = open("KEYIV.key", "rb")
input_data = input_file.read()
input_file.close()

cfb_cipher = AES.new(key0, AES.MODE_CFB, iv0)
enc_data = cfb_cipher.encrypt(input_data)

enc_file = open("KEYIV.key", "wb")
enc_file.write(enc_data)
enc_file.close()

print ("Completed Generating")
