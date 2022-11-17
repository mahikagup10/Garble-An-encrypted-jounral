from cryptography.fernet import Fernet


with open('test.txt', 'rb') as file:
    original = file.read()
data = original

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(data)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(bytes(encMessage))


print("original string: ",data.decode('utf-8'))
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()


 
print("decrypted string: ", decMessage)