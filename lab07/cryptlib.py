#Brian J Contois
#28 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#cryptlib.py

# Perform encryption logic here (message, shift offset)
# Creates the module 'encrypt' to be called for in caesar.py
# & test_cryptlib.py
def encrypt(message, shift):
    # Initialize variable 'encrypted_message'
    encrypted_message = ""
    # Is a single character in the message a letter or something else?
    for character in message:
        if character.isalpha():
            # Handle Uppercase Letters
            if character.isupper():
                base_ord = ord('A')
                position = ord(character) - base_ord
                new_position = (position + shift) % 26
                new_character = chr(new_position + base_ord)
                encrypted_message += new_character
            # Handle Lowercase Letters
            else:
                base_ord = ord('a')
                position = ord(character) - base_ord
                new_position = (position + shift) % 26
                new_character = chr(new_position + base_ord)
                encrypted_message += new_character
        else:
            # Preserve non-alphabetic characters
            encrypted_message += character
    # Process creates an encrypted message 
    # and displays it in the terminal
    return encrypted_message

# Perform decryption logic here (message, shift offset)
# Creates the module 'decrypt' to be called for in caesar.py 
# & test_cryptlib.py
def decrypt(message, shift):
    # Reversing encryption by applying a negative value 
    # to the shift offset applied during encryption
    decrypted_message = encrypt(message, -shift)
    # Process decrypts message entered, 
    # and displays the message in the terminal
    return decrypted_message

# Shout Out to John (Alias) for helping me

