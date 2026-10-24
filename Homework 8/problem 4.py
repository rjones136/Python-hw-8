# Homework 8 - Problem 4
# Date Shift Cipher

def encrypt(message, date):
    encrypted = ""
    position = 0

    for letter in message:
        shift = int(date[position % len(date)])
        number = ord(letter) - ord("A")
        new_number = (number + shift) % 26
        encrypted += chr(new_number + ord("A"))
        position += 1

    return encrypted


def decrypt(message, date):
    decrypted = ""
    position = 0

    for letter in message:
        shift = int(date[position % len(date)])
        number = ord(letter) - ord("A")
        new_number = (number - shift) % 26
        decrypted += chr(new_number + ord("A"))
        position += 1

    return decrypted


message = input("Enter a message: ")
date = input("Enter a date (MM/DD/YY): ")

message = message.replace(" ", "").upper()
date = date.replace("/", "")

encrypted_message = encrypt(message, date)
decrypted_message = decrypt(encrypted_message, date)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
