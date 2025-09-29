# initialize parameters for changeing a to 1
q_hex = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
q = int(q_hex, 16)
a = 1

print("Initialize public parameters:")
print("q: ", q)
print("a: ", a)
print()

# generate public keys and private keys
privateA = getPrivateKey(q)
privateB = getPrivateKey(q)

print("Private Key A: ", privateA)
print("Private Key B: ", privateB)
print()

# Ya
publicA = getPublicKey(q, a, privateA)
# Yb
publicB = getPublicKey(q, a, privateB)

print(f"A -------- sends public key ({publicA}) --------> B")
print(f"A <------- sends public key ({publicB}) --------- B")
print()

# alice and bob compute shared key
print("Compute A's shared key: ")
sharedKeyA = deriveKey(q, publicB, privateA)
print("Compute B's shared key: ")
sharedKeyB = deriveKey(q, publicA, privateB)

# mallory knows the shared key is derrived from 1 from the manipulation of a
print("Mallory computes the shared key:")
sharedKeyM = deriveKey(q, 1, 1)

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

# Mallory decrypts both messages
malloryA_decrypted = decrypt(msgA_encrypted, sharedKeyM)
malloryB_decrypted = decrypt(msgB_encrypted, sharedKeyM)

print("Mallory decrypt's A's message to using 0 as the key")
print(malloryA_decrypted.decode())
print()

print("Mallory decrypt's B's message to using 0 as the key")
print(malloryB_decrypted.decode())
print()
