from pqcrypto.kem import kyber512

# Generar un par de claves (clave pública y clave privada)
public_key, private_key = kyber512.keypair()

# Cifrar un mensaje usando la clave pública
ciphertext, shared_secret_enc = kyber512.enc(public_key)

# Descifrar el mensaje usando la clave privada
shared_secret_dec = kyber512.dec(ciphertext, private_key)

# Verificar que el secreto compartido es el mismo
assert shared_secret_enc == shared_secret_dec
print("El secreto compartido coincide:", shared_secret_enc.hex())