from Crypto.Cipher import AES
from Crypto import Random

import os, sys

def encrypt_it(bytefile, key, iv):
	cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
	return cfb_cipher.encrypt(bytefile)

def decrypt_it(bytefile, key, iv):
	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	return cfb_decipher.decrypt(bytefile)

def readBinFile(dir):
	with open(dir, "rb") as file:
		data = file.read()
	file.close()
	return data

def writeBinFile(dir, data):
	with open(dir, "wb") as file:
		file.write(data)
	file.close()

def safe_os(cmd):
	try:
		os.system(cmd)
	except:
		pass

def keyGenerate(key, iv):
	with open("KEYIV.key", "w") as f:
		f.write("key = %s \n iv = %s \n" %(key, iv))
	f.close()

	key_data = readBinFile("KEYIV.key")
	writeBinFile("KEYIV.key", key_data)


#KEYIV used for encrypting data
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size) #initialization vector

# print ("\nKEY:", key)
# print ("IV:", iv, "\n")

safe_os('mkdir 1ORIGINAL')
safe_os('mkdir 2ENCRYPTED')
safe_os('mkdir 3DECRYPTED')

print ("The program allows you to encrypt files")
print ("Please put the files you want to encrypt in \'1ORIGINAL\'")

temp = input ("Press \'Enter\' key to continue...")

# Creating txt with key and iv used for encryption
print ("Generating KEYIV for the recipient")
keyGenerate(key, iv)


print ("Retrieving files in 1ORIGINAL\n")
try:
	oriFile = os.listdir("1ORIGINAL")
except:
	raise Exception('Directory \'1ORIGINAL\' does not exist in the current directory')


print ("Beginning Encryption...\n")

for file in oriFile:
	print ("Encrypting", file)

	filedata = readBinFile("1ORIGINAL/"+file)
	writeBinFile("2ENCRYPTED/"+file+".enc", encrypt_it(filedata, key, iv))

	print ("Completed encrypting", file, "\n")

print ("Encryption successful\n")


print ("Retrieving files in 2ENCRYPTED\n")
try:
	inFiles = os.listdir("2ENCRYPTED")
except:
	raise Exception('Directory \'2ENCRYPTED\' does not exist in the current directory')


print ("Beginning Decryption...\n")

for file in inFiles:
	print ("Decrypting", file)

	filedata = readBinFile("2ENCRYPTED/"+file)
	writeBinFile("3DECRYPTED/"+file[:-4], decrypt_it(filedata, key, iv))

	print ("Completed decrypting", file, "\n")

print ("Decryption successful\n")
