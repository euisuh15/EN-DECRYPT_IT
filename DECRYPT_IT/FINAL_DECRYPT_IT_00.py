from Crypto.Cipher import AES
from Crypto import Random

import os, sys

def decrypt_it(bytefile, key, iv):
	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	return cfb_decipher.decrypt(bytefile)

def readBinFile(dir):
	file = open(dir, "rb")
	data = file.read()
	file.close()
	return data

def writeBinFile(dir, data):
	file = open(dir, "wb")
	file.write(data)
	file.close()

def safe_os(cmd):
	try:
		os.system(cmd)
	except:
		pass

print ("The program allows you to decrypt files")
print ("Please put the key file you have received from the sender in the current directory")
temp = input ("Press \'Enter\' key to continue...\n")

try:
	plain_key = readBinFile("KEYIV.key")
except:
	raise Exception('KEYIV.key does not exist in the current directory')

#Retrieving KEY and IV used for decryption
print ("Retrieving KEYIV")

try:
	keyiv = open("KEYIV.key", 'r')
	ki = keyiv.readlines()
	keyiv.close()
except:
	raise Exception('KEYIV.key does not exist in the current directory')

print ("Retrieving completed\n")

exec("key = "+ ki[0][6:-2])
exec("iv = " + ki[1][5:-2])

safe_os('mkdir 1ENCRYPTED')
safe_os('mkdir 2DECRYPTED')

print ("Please put the files you want to decrypt in \'1ENCRYPTED\'")
temp = input ("Press \'Enter\' key to continue...")

#Begin decryption
print ("Retrieving files in 1ENCRYPTED")
try:
	inFiles = os.listdir("1ENCRYPTED")
except:
	raise Exception('Directory \'1ENCRYPTED\' does not exist in the current directory')

print ("Beginning Decryption...\n")

for file in inFiles:
	print ("Decrypting", file)

	filedata = readBinFile("1ENCRYPTED/"+file)
	writeBinFile("2DECRYPTED/"+file[:-4], decrypt_it(filedata, key, iv))

	print ("Completed decrypting", file, "\n")

print ("Decryption Completed\n")
