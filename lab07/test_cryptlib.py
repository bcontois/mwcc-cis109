#Brian J Contois
#28 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#test_cryptlib.py

# Importing modules created in the cryptlib.py file
from cryptlib import encrypt, decrypt

# Defining tests using the assert command on user created modules from cryptlib.py
# If the module does not do exactly as stated here in parameters given
# They fail the test. Otherwise, they PASS! :)

# Encryption test, shift by 3
def test_encrypt():
    assert encrypt("ABC", 3) == "DEF"

# Decryption test, shift by 3
def test_decrypt():
    assert decrypt("DEF", 3) == "ABC"

# Testing if the alphabet will go from Z to A
# And continue in a circular fashion
def test_wraparound():
    assert encrypt("XYZ", 3) == "ABC"

# Testing if lowercase letters will be correctly encrypted
def test_lowercase():
    assert encrypt("abc", 2) == "cde"

# Testing if non alpha items are kept intact through encryption
def test_preserve_spaces_and_numbers():
    assert encrypt("Hello World 123!", 3) == "Khoor Zruog 123!"

# Testing if the decryption function works
def test_decrypt_restores_original():
    message = "Hello World!"
    encrypted = encrypt(message, 5)
    assert decrypt(encrypted, 5) == message

# Shout Out to John (Alias) for helping me