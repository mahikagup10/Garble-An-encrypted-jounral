from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# def acceptKey():
#     key_string = input("Enter key of 16 characters:")
#     if len(key_string)!=16:
#         raise Exception("Key length not 16")
#     key = bytes(key_string, 'utf-8')
#     #print(key)
#     return key

def encryptText(key,data):
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(data)
    #print("Ciphertext:",ciphertext)
    return ciphertext,nonce

def decryptText(key,ciphertext,nonce):
    # key = acceptKey()
    # ciphertext,nonce = encryptText()
    cipher = AES.new(key,AES.MODE_EAX,nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode()
    #print("Plaintext:",plaintext)
    return plaintext


passw = input("Enter your key:")

with open("passwd.txt", 'rb') as pw:
    password = pw.read()

if passw.encode()!= password:
    print("incorrect key entered")
    exit()

key = get_random_bytes(16)
    
#data = "hi this needs to be encrypted".encode()
with open('test.txt', 'rb') as file:
    original = file.read()
data = original
#data = input("Enter diary entry:").encode()
# key = acceptKey()
ct,nonce = encryptText(key,data)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(bytes(ct))

print("Encrypted text:", ct)



pt = decryptText(key,ct,nonce)
print("Decrypted text:", pt)

# with open('test.bin', 'rb') as enc_file:
    # encrypted = enc_file.read()

# decrypted = decryptText(key,ct,nonce)

with open('test.txt', 'wb') as dec_file:
    dec_file.write(pt.encode())





