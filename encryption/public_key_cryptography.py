import base64
import os
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__).parent[2]
PRIVATE_KEY_FILE = Path(PROJECT_FOLDER) / "my_keypair"
PUBLIC_KEY_FILE = Path(PROJECT_FOLDER) / "my_keypair.pub"

# Load the private key from file
with open(PRIVATE_KEY_FILE, "r") as key_file:
    private_key = RSA.import_key(key_file.read())

# Generate public key from the private key
public_key = private_key.publickey()
