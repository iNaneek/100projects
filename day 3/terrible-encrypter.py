import random  # uncrackable encrypting, even with a key
inp = list(input("Text to encrypt: "))
#
enc = ''
for i in range(len(inp)):
    enc += chr(random.randint(0,66))

print(enc)