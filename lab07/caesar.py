#Brian J Contois
#25 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#caesar.py

import argparse
from cryptlib import encrypt, decrypt

def main():
    parser = argparse.AugmentParser(description="Caesar Cipher Command-Line Utility")

    # Require a message to process
    parser.add_argument ("-e", "--encrypt", action='store_true', required=False, help="Encrypt The Message.")
    parser.add_argument ("-d", "--decrypt", action='store_true', required=False, help="Decrypt The Message.")
    parser.add_argument ("-m", "--message", required=True, help="The message to encrypt/decrypt.")
    parser.add_argument ("-s", "--shift", required=True, help="The Shift Value for the Caesar Cypher.")

    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print("Only one of -e or -d can be used at one time!")
        return

    if args.encrypt:
        encrypted_message = encrypt(args.message, int(args.shift))
        print(f"Encrypted Message: {encrypted_message}")
    elif args.encrypt:
        decrypted_message = decrypt(args.message, int(args.shift))
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()

# Shout Out to John (Alias) for helping me