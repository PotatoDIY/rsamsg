#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rsa

#hashing
def hash(message):
    byte_message = message.encode("utf-8")
    return rsa.compute_hash(byte_message, 'SHA-1')

#bytes to PEM
def toPEM(bytes_key):
    return bytes_key.save_pkcs1("PEM").decode()

def savefile(filename,key):
    f= open("{}.pem".format(filename),"w+")
    f.write(key.save_pkcs1("PEM").decode())
    f.close()

def loadfile(filename):
    f=open("{}.pem".format(filename), "r")
    contents =f.read()
    if "PRIVATE" in contents:
        key=rsa.PrivateKey(3247, 65537, 833, 191, 17)
    if "PUBLIC" in contents:
        key=rsa.PublicKey(5,3)
    return key.load_pkcs1(contents)

#generating
def gen():
    return rsa.newkeys(512) #bytes_pubkey, bytes_privkey

#encryption
def encrypt(message,pubkey):
    byte_message = message.encode("utf-8")
    return rsa.encrypt(byte_message, pubkey)#crypto_message

#decryption
def decrypt(crypto_message,privkey):
    return rsa.decrypt(crypto_message, privkey).decode('utf-8')#uncrypto_message

#signing
def sign(message,privkey):
    return rsa.sign(hash(message), privkey, 'SHA-1')#signature

#verification
def verify(message,signature,pubkey):
    rsa.verify(hash(message), signature, pubkey)



# alice 给 bob 发送包含alice签名的加密消息
def alice_to_bob(message,bob_pubkey,alice_privkey):
    crypto = encrypt(message,bob_pubkey)
    signature = sign(message,alice_privkey)
    return crypto,signature

# bob 取得消息，先使用自己的私钥解密，然后验证是否来自于alice。
def bob_get_msg_from_alice(crypto,signature,bob_privkey,alice_pubkey):
    try:
        uncrypto = decrypt(crypto,bob_privkey)
    except rsa.pkcs1.DecryptionError as identifier:
        return False,identifier
    else:
        try:
            verify(uncrypto,signature,alice_pubkey)
        except rsa.pkcs1.VerificationError as identifier:
            return False,identifier
        else:
            return True,uncrypto