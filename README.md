# AES-256 Encryption Tool

## Overview
This Python script provides a robust encryption and decryption tool using the **AES-256 algorithm** in **CFB mode**. It allows secure encryption of text messages and their decryption using a unique key.

## Features
- Generates a **256-bit encryption key**.
- Uses **AES-256 encryption with CFB (Cipher Feedback) mode**.
- Supports **base64 encoding** for easy storage and transmission.

## Prerequisites
- Python 3.x installed
- `cryptography` library installed

### Install the required library:
```bash
pip install cryptography
```

## How to Use
1. Run the script to generate an encryption key and encrypt the message:
   ```bash
   python encryption_tool.py
   ```

2. The script will display the encrypted and decrypted messages:
```
Encrypted: [Encrypted text in base64 format]
Decrypted: This is a secret message.
```

## How It Works
1. **Key Generation:** A 256-bit key is generated using `os.urandom()`.
2. **Encryption:** The script creates an AES cipher with a 128-bit IV (Initialization Vector) and encrypts the message.
3. **Base64 Encoding:** The encrypted data (IV + ciphertext) is encoded for easier handling.
4. **Decryption:** The IV and ciphertext are extracted from the base64 data and decrypted back to the original message.

## Limitations
- This script is for educational purposes and should not be used in production without additional security measures.
- The encryption key is generated every time the script runs, making it impossible to decrypt past messages without the original key.

## Future Enhancements
- Add file encryption support.
- Implement secure key management.

## License
MIT License

