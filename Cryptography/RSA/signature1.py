# so signing signature is a way to stop man in the middle when sending
# a public key over an insecure channel


import os
import json
import time


# formulas

# my friend can decrypt the message using their private key
# m = c^d mod N
# where c is the ciphertext, d is the private exponent, and N is the modulus
# using my public key they calculate s=s^e mod N
# where s is the signature, e is the public exponent, and N is the modulus

#now to ensure that the message was not intercepted/modified
# they can compute H(m) and compare it to s: assert H(m) == s

# now given a private key and sha256 hash function sign this flag
# sign this flag: FLAG{crypto{Immut4ble_m3ssag1ng}}
# using my private key generate a signature for the flag

from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long

#u can put your N and d here
N = int("")  
d = int("")
# message must match EXACTLY what the challenge says
msg = b"crypto{Immut4ble_m3ssag1ng}"

h_bytes = SHA256.new(msg).digest()
h = bytes_to_long(h_bytes)

s = pow(h, d, N)

#s is the answer
print(s)              # most challenges want this decimal integer
print(hex(s))         # helpful in case they want hex







# def generate_rsa_keypair(bits=2048):
#     key = RSA.generate(bits)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return private_key, public_key

# def sign_public_key(private_key, public_key):
#     key = RSA.import_key(private_key)
#     h = SHA256.new(public_key)
#     signature = pkcs1_15.new(key).sign(h)
#     return b64encode(signature).decode('utf-8')

# def verify_signature(public_key, signature, public_key_to_verify):
#     key = RSA.import_key(public_key)
#     h = SHA256.new(public_key_to_verify)
#     try:
#         pkcs1_15.new(key).verify(h, b64decode(signature))
#         return True
#     except (ValueError, TypeError):
#         return False
    
# def main():
#     # Generate RSA key pair for Alice
#     alice_private_key, alice_public_key = generate_rsa_keypair()
    
#     # Alice signs her public key
#     signature = sign_public_key(alice_private_key, alice_public_key)
    
#     # Save Alice's public key and signature to a file (simulating sending over insecure channel)
#     with open('alice_public_key.json', 'w') as f:
#         json.dump({
#             'public_key': alice_public_key.decode('utf-8'),
#             'signature': signature
#         }, f)
    
#     # Simulate Bob receiving Alice's public key and signature
#     with open('alice_public_key.json', 'r') as f:
#         data = json.load(f)
#         received_public_key = data['public_key'].encode('utf-8')
#         received_signature = data['signature']
    
#     # Bob verifies the signature
#     is_valid = verify_signature(alice_public_key, received_signature, received_public_key)
    
#     if is_valid:
#         print("Signature is valid. Public key is authentic.")
#     else:
#         print("Signature is invalid. Public key may have been tampered with.")

# if __name__ == "__main__":
#     main()
# print(pow(101, 17, 22663))
# print(pow(base, exp, modulus))