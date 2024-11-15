# %%
# Import the Caesar Cipher - one of the oldest and simplest forms of encryption
# It works by shifting each letter in the alphabet by a fixed number (the offset/key)
from caesarcipher import CaesarCipher

# %%
# Simple example showing how the cipher works:
# With offset=1, 'a' becomes 'b', 'b' becomes 'c', etc.
# Notice it handles spaces, numbers, and capital letters
CaesarCipher("abcdefg xyz 2035 MMXXXV", offset=1).encoded

# %%
# In symmetric encryption, both sender and receiver share the same secret key
OUR_SHARED_SECRET = 5  # This is our encryption/decryption key (offset)

# Message we want to encrypt
original_message = "There are 42 figs in the basket I sent you, Claudius."

# Encrypt the message using our shared secret as the offset
encoded = CaesarCipher(original_message, offset=OUR_SHARED_SECRET).encoded

# Print both messages to see the difference
print(f"Original message: {original_message}")
print(f"Encrypted message: {encoded}")

# %%
# To decrypt, we use the same shared secret (key)
# This demonstrates why it's called "symmetric" - same key for encryption and decryption
decoded = CaesarCipher(encoded, offset=OUR_SHARED_SECRET).decoded
print(f"Decrypted message: {decoded}")

# Key concepts demonstrated:
# 1. Symmetric encryption uses the same key for encryption and decryption
# 2. The key must be kept secret and shared securely between parties
# 3. Even a simple shift cipher shows how plain text can be made unreadable
# 4. The algorithm is public, but without the key, decryption is difficult

# Try it yourself:
# 1. Change the OUR_SHARED_SECRET to another number
# 2. Try encrypting your own messages
# 3. What happens if you use the wrong key for decryption?
# 4. Can you figure out why this isn't secure for real-world use?
# %%
