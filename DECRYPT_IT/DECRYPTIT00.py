from Crypto.Cipher import AES
from Crypto import Random

import os, sys

#Fix ME!
key = b'\x18X\xfd&\xdb\xfdd5\xa9\xc4\xb0I\x8b\xda\xd8\x00'
iv = b'\x03=\xb0Is\xec\n\xbd\xb2\xbcU\xbfS\xe7\xfc\xdc'

inFiles = os.listdir("2ENCRYPTED")

for file in inFiles:

	enc_file2 = open("2ENCRYPTED/"+file, "rb")
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	output_file = open("3DECRYPTED/"+file[:-4]+".jpg", "wb")
	output_file.write(plain_data)
	output_file.close()
