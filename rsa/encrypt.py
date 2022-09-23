import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


key_pair = RSA.generate(2048)

message = "A message for encryption".encode()
cipher = PKCS1_OAEP.new(key_pair)

encrypted = cipher.encrypt(message)
print("Encrypted:", binascii.hexlify(encrypted))

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())