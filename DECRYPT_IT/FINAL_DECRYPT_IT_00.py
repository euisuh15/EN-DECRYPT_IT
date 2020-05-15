from Crypto.Cipher import AES
from Crypto import Random

import os, sys

print ("The program allows you to decrypt files")
print ("Please put the key file you have received from the sender in the current directory")
temp = input ("Press \'Enter\' key to continue...\n")

#Retrieving KEY and IV used for decryption
print ("Retrieving KEYIV")

try:
	keyiv = open ("KEYIV.key", 'r')
	ki = keyiv.readlines()
	keyiv.close()
except:
	raise Exception('KEYIV.key does not exist in the current directory')

print ("Retrieving completed\n")

exec("key = "+ ki[0][6:-2])
exec("iv = " + ki[1][5:-2])

try:
	os.system('mkdir 1ENCRYPTED')
except:
	pass

print ("Please put the files you want to decrypt in \'1ENCRYPTED\'")
temp = input ("Press \'Enter\' key to continue...")

#Begin decryption
print ("Retrieving files in 1ENCRYPTED")

try:
	inFiles = os.listdir("1ENCRYPTED")
except:
	raise Exception('Directory \'1ENCRYPTED\' does not exist in the current directory')

print ("Retrieving completed")
print ("Beginning Decryption\n")

for file in inFiles:
	print ("Decrypting", file)

	enc_file2 = open("1ENCRYPTED/"+file, "rb")
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	try:
		os.system('mkdir 2DECRYPTED')
	except:
		pass

	output_file = open("2DECRYPTED/"+file[:-4], "wb")
	output_file.write(plain_data)
	output_file.close()
	print ("Completed decrypting", file, "\n")

print ("Decrypting Completed\n")
