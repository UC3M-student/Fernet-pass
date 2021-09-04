from cryptography.fernet import Fernet

key = b" Import key  "
f = Fernet(key)
encrypted = b" ENCRIPTED MESSAGE "
decrypted = f.decrypt(encrypted)
print(decrypted) #Message
