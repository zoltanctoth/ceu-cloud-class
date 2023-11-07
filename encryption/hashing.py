# %%
import hashlib

# %%
print("Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓")

# %%
print("Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓".encode("utf-8"))

# %%


# Simple hashing function equivalent to the R example
def naivehash(val):
    return sum(ord(c) for c in val) % 100


print(naivehash("Hello Hashed Message!"))
print(naivehash("Hello Hashed Message 2!"))

# %%
# Hashing using SHA-256
hashed_message = hashlib.sha256(
    "Say Hallo to a better hash!".encode("utf-8")
).hexdigest()
print(hashed_message)
print("The SHA-256 hash is {} characters long".format(len(hashed_message)))
print("Number of possible hashes: {}".format(16 ** len(hashed_message)))


# %%
