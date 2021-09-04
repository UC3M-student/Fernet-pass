from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#print(key)

#file = open("key.txt", "wb")
#file.write(key)
#file.close()

file = open("key.txt", "rb")
key = file.read()
file.close()
print(key)
encoded = message.encode() # Message in bytes
f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)


