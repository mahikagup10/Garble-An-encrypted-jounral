from Crypto.Cipher import AES

def acceptKey():
    key_string = input("Enter key of 16 characters:")
    if len(key_string)!=16:
        raise Exception("Key length not 16")
    key = bytes(key_string, 'utf-8')
    #print(key)
    return key

def encryptText(key,data):
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
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
    
#data = "hi this needs to be encrypted".encode()
data = input("Enter diary entry:").encode()
key = acceptKey()
ct,nonce = encryptText(key,data)
pt = decrypt(key,ct,nonce)
print("Encrypted text:", ct)
print("Decrypted text:", pt)

