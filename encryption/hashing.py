# %%
import hashlib  # Python's standard library for various hash algorithms

# %%
# Let's look at a message that contains Unicode characters - any modern text!
message = "Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓"
print(message)

# %%
# To hash something, we first need to convert it to bytes using UTF-8 encoding
# Hash functions work on bytes, not strings
bytestring = "Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓".encode("utf-8")
print(bytestring)

# %%
# We can always convert bytes back to a string - UTF-8 encoding is reversible
print("Say hi again! " + bytestring.decode("utf-8"))


# %%
# Here's a simple (and very insecure!) hash function to understand the concept
# Remember: This is for learning only - never use this in real applications!
def naivehash(val):
    # We just sum the ASCII values of characters and take modulo 100
    return str(sum(ord(c) for c in val) % 100)


# See how similar messages produce different hashes
print("Hash of 'Hello Hashed Message!':   " + naivehash("Hello Hashed Message!"))
print("Hash of 'Hello Hashed Message 2!': " + naivehash("Hello Hashed Message 2!"))

# %%
# Now let's use SHA-256, a real cryptographic hash function
# SHA-256 is what you'll use in real applications because it:
# - Always outputs 256 bits (shown as 64 hex characters)
# - Practically eliminates chance of collisions
# - Can't be reversed to find your input
# - Changes completely even if input changes slightly

bytestring = "My message to the world: Say Hällo to a better hash!".encode("utf-8")
print("Original message: ")
print(bytestring)

# Create hash and convert to hexadecimal string
hashed_message = hashlib.sha256(bytestring).hexdigest()
print()
print("Hash: " + hashed_message)

# %%
# Watch how a tiny change (just capitalizing one letter)
# creates a completely different hash!
message1 = "hello"
message2 = "Hello"

hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()

print(f"Message 1: {message1}")
print(f"Hash 1:    {hash1}")
print()
print(f"Message 2: {message2}")
print(f"Hash 2:    {hash2}")

# Even though the messages differ by just one bit,
# the hashes are entirely different. This is a key
# feature of cryptographic hash functions called
# the "avalanche effect"

# %%
# Let's look at the scale of SHA-256:
# Each hash is 64 characters, and the number of possible values is enormous
print(f"The SHA-256 hash is always {len(hashed_message)} characters long and it can take the values 0-9a-f.")
print(f"Number of possible hashes: {16 ** len(hashed_message)}")

# %%
