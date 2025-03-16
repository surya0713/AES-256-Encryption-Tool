from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64


def generate_key():
    return os.urandom(32)  # 256-bit key


def encrypt_message(key, plaintext):
    iv = os.urandom(16)  # 128-bit IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_message(key, encrypted_text):
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode('utf-8')


if __name__ == "__main__":
    key = generate_key()
    message = "This is a secret message."

    encrypted = encrypt_message(key, message)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(key, encrypted)
    print("Decrypted:", decrypted)
