# %%
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__).parent.parent
PRIVATE_KEY_FILE = PROJECT_FOLDER / "my_keypair"
PUBLIC_KEY_FILE = PROJECT_FOLDER / "my_keypair.pub"

assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)

# %%

# Load the private key from file
with open(PRIVATE_KEY_FILE, "r") as key_file:
    private_key = RSA.import_key(key_file.read())

# Generate public key from the private key
public_key = private_key.publickey()


# %%
short_secret_message = "My Secret Message".encode("utf-8")
public_key_cipher = PKCS1_OAEP.new(public_key)
encrypted_message = public_key_cipher.encrypt(short_secret_message)
print(f"Encrypted message: {encrypted_message}")

ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "encrypted_message.bin"
with open(ENCRYPTED_MESSAGE_FILE, "wb") as f:
    f.write(encrypted_message)

# %%
with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    encrypted_message_from_file = f.read()

private_key_cipher = PKCS1_OAEP.new(private_key)
decrypted_message = private_key_cipher.decrypt(encrypted_message_from_file)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
