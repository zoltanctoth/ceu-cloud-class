# %%
from caesarcipher import CaesarCipher

# %%
CaesarCipher("abcdefg xyz 2035 MMXXXV", offset=1).encoded

# %%
OUR_SHARED_SECRET = 5
original_message = "There are 42 figs in the basket I sent you, Claudius."
encoded = CaesarCipher(original_message, offset=OUR_SHARED_SECRET).encoded
print(f"Original message: {original_message}")
print(f"Encrypted message: {encoded}")

# %%
decoded = CaesarCipher(encoded, offset=OUR_SHARED_SECRET).decoded
print(f"Decrypted message: {decoded}")
