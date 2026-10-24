# Homework 8 - Problem 5
# Keyword Cipher

def encrypt(message, alphabet, cipher):
    encrypted = ""

    for letter in message:
        position = alphabet.find(letter)
        if position != -1:
            encrypted += cipher[position]
        else:
            encrypted += letter

    return encrypted


def decrypt(message, alphabet, cipher):
    decrypted = ""

    for letter in message:
        position = cipher.find(letter)
        if position != -1:
            decrypted += alphabet[position]
        else:
            decrypted += letter

    return decrypted


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

keyword = input("Enter a keyword: ").upper()
message = input("Enter a message: ").upper()

cipher = ""

# Add each unique letter from the keyword
for letter in keyword:
    if letter in alphabet and letter not in cipher:
        cipher += letter

# Add the remaining letters of the alphabet
for letter in alphabet:
    if letter not in cipher:
        cipher += letter

encrypted_message = encrypt(message, alphabet, cipher)
decrypted_message = decrypt(encrypted_message, alphabet, cipher)

print("\nOriginal Alphabet:", alphabet)
print("Cipher Alphabet:  ", cipher)
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
