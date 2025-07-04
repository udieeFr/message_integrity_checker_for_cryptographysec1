from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import os

# generate key - THIS IS NOW UNCOMMENTED
# def generate_key():

#     # buat folder utk keys if not exist
#     os.makedirs("key", exist_ok=True)

#     private_key = RSA.generate(2048)
#     with open ("key/private_key.key", "wb") as key_file:
#         key_file.write(private_key.export_key())

#     # public key kena derived from private key
#     public_key = private_key.publickey()
#     with open ("key/public_key.key", "wb") as key_file:
#         key_file.write(public_key.export_key())

def hash_message(msg):
    hashed_message = SHA256.new(msg.encode())
    return hashed_message

def sign_message(message, hashed_msg):
    key = RSA.import_key(open('key/private_key.key').read())
    signer = pkcs1_15.new(key)
    signature = signer.sign(hashed_msg)

    with open ("signed_message.txt", "a") as signing:
        signing.write(f"{message} | {signature.hex()}\n")

    return signature

def verify():
    key = RSA.import_key(open("key/public_key.key").read())

    with open ("signed_message.txt", "r") as read_message:
        stored_message = read_message.readlines()
        for lines in stored_message:
            lines = lines.strip()
            message, signature = map(str.strip, lines.split("|", 1))
            

            msg_second_hash = SHA256.new(message.encode())

            signature_bytes = bytes.fromhex(signature.strip())

            try:
                pkcs1_15.new(key).verify(msg_second_hash, signature_bytes)
                print("The signature is valid, Message has not been tempered with.")
            except (ValueError, TypeError):
                print(f"This is not the original messages, your message has been tempered and changed into \"{message}\" sir !!!")
    
    

    