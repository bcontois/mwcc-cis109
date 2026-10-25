#Brian J Contois
#25 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#cryptlib.py

def encrypt(message, shift):
    encrypted_message = ""
    for character in message:
        if character.isalpha():
            # Perform encryption logic here
            if character.isupper():
                base_ord = ord('A')
                #Handle Uppercase letters
            else:
                base_ord = ord('a')
            position = ord(character) - base_ord
            new_position = (position + shift) % 26
            new_character = chr(new_position + base_ord)
            encrypted_message += new_character
        else:
            # Preserve non-alphabetic characters
            encrypted_message += new_character

    def decrypt(message, shift):
        decrypted_message = encrypt(message,-shift)
        return decrypted_message

# Shout Out to John (Alias) for helping me

