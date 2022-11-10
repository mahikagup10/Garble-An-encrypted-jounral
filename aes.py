from Crypto.Cipher import AES


def acceptKey():
    key_string = input("Enter key of 16 characters:")
    key = bytes(key_string, 'utf-8')
    #print(key)
    return key

#mahika
# key= b'C&F)H@McQfTjWnZr'
def encryptText(key):
    #key = acceptKey()
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    data = "hi this needs to be encrypted".encode()
    ciphertext = cipher.encrypt(data)
    #print("Ciphertext:",ciphertext)
    return ciphertext,nonce

def decrypt(key,ciphertext,nonce):
    # key = acceptKey()
    # ciphertext,nonce = encryptText()
    cipher = AES.new(key,AES.MODE_EAX,nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode()
    #print("Plaintext:",plaintext)
    return plaintext
    

key = acceptKey()
ct,nonce = encryptText(key)
pt = decrypt(key,ct,nonce)
print("Encrypted text:", ct)
print("Decrypted text:", pt)

