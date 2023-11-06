import os
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    Encoding, PublicFormat, PrivateFormat, NoEncryption)
from base64 import urlsafe_b64encode

def generate_vapid_key_pair_bit_length():
    private_key = ec.generate_private_key(ec.SECP256R1(), os.urandom)
    private_pem = private_key.private_bytes(Encoding.PEM,
                                            PrivateFormat.PKCS8,
                                            NoEncryption())
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(Encoding.PEM,
                                         PublicFormat.SubjectPublicKeyInfo)
    public_key_uncompressed = public_key.public_bytes(Encoding.X962,
                                                       PublicFormat.UncompressedPoint)[1:]

    return {
        'private': private_pem,
        'public': public_pem,
        'public_uncompressed': urlsafe_b64encode(public_key_uncompressed)
    }

keys = generate_vapid_key_pair_bit_length()
with open("private_key.pem", "wb") as f:
    f.write(keys['private'])

with open("public_key.pem", "wb") as f:
    f.write(keys['public'])

print("Public Key (uncompressed):", keys['public_uncompressed'].decode())