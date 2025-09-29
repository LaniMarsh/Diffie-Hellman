# initialize parameters
q = 37
a = 5
print("Initialize public parameters:")
print("q: ", q)
print("a: ", a)
print()

# generate public keys and private keys
privateA = getPrivateKey(q)
privateB = getPrivateKey(q)
publicA = getPublicKey(q, a, privateA)
publicB = getPublicKey(q, a, privateB)

print("Private Key A: ", privateA)
print("Private Key B: ", privateB)
print()

print(f"A -------- sends public key ({publicA}) --------> B")
print(f"A <------- sends public key ({publicB}) --------- B")
print()

# compute shared key
print("Compute A's shared key: ")
sharedKeyA = deriveKey(q, publicB, privateA)
print("Compute B's shared key: ")
sharedKeyB = deriveKey(q, publicA, privateB)

print()

print("A's shared key: ", sharedKeyA)
print("B's shared key: ", sharedKeyB)
print()

# A sends message to B
msgA = "Hi Bob!"
msgA_encrypted = encrypt(msgA.encode(), sharedKeyA)

print("A's message: ", msgA)
print("A's encrypted message: ", msgA_encrypted)
print()

msgA_decrypted = decrypt(msgA_encrypted, sharedKeyA)
print("B decrypts A's message using B's key")
print(msgA_decrypted.decode())
print()

# B sends message to A
msgB = "Hi Alice!"
msgB_encrypted = encrypt(msgB.encode(), sharedKeyB)

print("B's message: ", msgB)
print("B's encrypted message: ", msgB_encrypted)
print()

msgB_decrypted = decrypt(msgB_encrypted, sharedKeyB)
print("A decrypt's B's message to using A's key")
print(msgB_decrypted.decode())
print()
