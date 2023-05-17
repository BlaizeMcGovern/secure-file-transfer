import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

private_key_path = os.getenv('PRIVATE_KEY_PATH')
public_key_path = os.getenv('PUBLIC_KEY_PATH')

# Generate RSA key pair
key = paramiko.RSAKey.generate(2048)

# Save the private key to file
key.write_private_key_file(private_key_path)

# Save the public key to file
with open(public_key_path, 'w') as f:
    f.write(key.get_base64())

# Use the keys as needed
# ...
