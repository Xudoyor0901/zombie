import ecdsa
import os

# Generate a new private key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Derive the corresponding public key
public_key = private_key.get_verifying_key()

# Get the public key in uncompressed form (starting with "04")
uncompressed_public_key = public_key.to_string('uncompressed')

# Generate a message to sign
message = os.urandom(32)

# Sign the message using the private key
signature = private_key.sign(message)

# Verify the signature using the public key
is_valid = public_key.verify(signature, message)

# Print the results
print(f"Private key: {private_key.to_string().hex()}")
print(f"Public key: {uncompressed_public_key.hex()}")
print(f"Message: {message.hex()}")
print(f"Signature: {signature.hex()}")
print(f"Is valid signature? {is_valid}")
