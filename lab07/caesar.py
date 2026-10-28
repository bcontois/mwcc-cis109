#Brian J Contois
#28 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#caesar.py

# Importing argparse module for command line argument inputs 
import argparse

# Importing modules created in the cryptlib.py file
from cryptlib import encrypt, decrypt

# Main Module caesar.py to utilize user created modules from cryptlib.py
# To encrypt and decrypt a message entered on the command line
def main():
    parser = argparse.ArgumentParser()

    # Requires a message to encrypt or decrypt depending on the value of the shift entered.
    parser.add_argument ("-e", "--encrypt", action='store_true', required=False, help="Encrypt The Message.")
    parser.add_argument ("-d", "--decrypt", action='store_true', required=False, help="Decrypt The Message.")
    parser.add_argument ("-m", "--message", required=True, help="The message to encrypt/decrypt.")
    parser.add_argument ("-s", "--shift", required=True, help="The Shift Offest Value for the Caesar Cypher.")
    args = parser.parse_args()

    # Input cannot have both encrypt and decrypt performed
    if args.encrypt and args.decrypt:
        print("Only one of -e or -d can be used at one time!")
        return

    # Input message gets encrypted if -e flag is entered 
    # (Message input, Shift offest input)
    # Encrypted message is displayed in the terminal
    if args.encrypt:
        encrypted_message = encrypt(args.message, int(args.shift))
        print(f"Encrypted Message: {encrypted_message}")

    # Input message gets decrypted if -d flag is entered 
    # (Message input, Shift offset input)
    # Decrypted message is displayed in the terminal    
    elif args.decrypt:
        decrypted_message = decrypt(args.message, int(args.shift))
        print(f"Decrypted Message: {decrypted_message}")

# MAIN
if __name__ == "__main__":
    main()

# Shout Out to John (Alias) for helping me