# %%
from pathlib import Path

# RSA encryption modules from pycryptodome library
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Define paths for our key files
PROJECT_FOLDER = Path(__file__).parent.parent
PRIVATE_KEY_FILE = PROJECT_FOLDER / "my_keypair"  # Contains the private key
PUBLIC_KEY_FILE = PROJECT_FOLDER / "my_keypair.pub"  # Contains the public key

# Make sure our key files exist before proceeding
assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)

# %%
# Load the private key from file
# The private key must be kept secret and secure
with open(PRIVATE_KEY_FILE, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())

# Extract the public key from our private key
# The public key can be freely shared with anyone
public_key = private_key.publickey()
print(f"Public key:\n{public_key.export_key().decode('utf-8')}")

# %%
# Message to be encrypted - must be converted to bytes
short_secret_message = "My Secret Message".encode("utf-8")

# Create a cipher object using the public key for encryption
public_key_cipher = PKCS1_OAEP.new(public_key)

# Encrypt our message - only someone with the private key can decrypt it
encrypted_message = public_key_cipher.encrypt(short_secret_message)
print(f"Encrypted message:")
print(encrypted_message)

# Save the encrypted message to a file
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "encrypted_message.bin"
with open(ENCRYPTED_MESSAGE_FILE, "wb") as f:
    f.write(encrypted_message)

# %%
# Read the encrypted message from file
with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    encrypted_message_from_file = f.read()

# Create a cipher object using the private key for decryption
private_key_cipher = PKCS1_OAEP.new(private_key)

# Decrypt the message using the private key
decrypted_message = private_key_cipher.decrypt(encrypted_message_from_file)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")

# This demonstrates asymmetric encryption where:
# 1. Messages are encrypted with a public key and can only be decrypted with the matching private key
# 2. The public key can be freely shared
# 3. The private key must be kept secret
# 4. This is more secure than symmetric encryption as the decryption key (private key) is never shared

# %%
