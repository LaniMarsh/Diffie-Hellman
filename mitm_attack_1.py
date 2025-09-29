# initialize parameters
q_hex = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
q = int(q_hex, 16)
a_hex = "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5"
a = int(a_hex, 16)

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

# Mallory makes Ya and Yb q instead of getting the public key
# Ya
Ya = getPublicKey(q, a, privateA)
publicA = q
# Yb
Yb = getPublicKey(q, a, privateB)
publicB = q

print(f"A -------- sends public key ({publicA}) --------> B")
print(f"A <------- sends public key ({publicB}) --------- B")
print()

# alice and bob compute shared key
print("Compute A's shared key: ")
sharedKeyA = deriveKey(q, publicB, privateA)
print("Compute B's shared key: ")
sharedKeyB = deriveKey(q, publicA, privateB)

# mallory knows the shared key is 0
print("Mallory computes the shared key:")
# sharedKeyM = deriveMalloryKey(0)
sharedKeyM = deriveKey(q, q, 4)

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

print("Mallory decrypt's A's message to B using 0 as the key")
print(malloryA_decrypted.decode())
print()

print("Mallory decrypt's B's message to A using 0 as the key")
print(malloryB_decrypted.decode())
print()

