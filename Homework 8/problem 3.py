# Homework 8 - Problem 3
# Scytale Cipher

def encrypt(message, rows):
    columns = len(message) // rows
    encrypted = ""

    for row in range(rows):
        for column in range(columns):
            position = column * rows + row
            encrypted += message[position]

    return encrypted


def decrypt(message, rows):
    columns = len(message) // rows
    decrypted = ""

    for column in range(columns):
        for row in range(rows):
            position = row * columns + column
            decrypted += message[position]

    return decrypted


message = input("Enter a message: ")
message = message.replace(" ", "").upper()

rows = int(input("Enter the number of rows: "))

while rows <= 0:
    rows = int(input("Enter a positive number of rows: "))

while len(message) % rows != 0:
    message += "X"

encrypted_message = encrypt(message, rows)
decrypted_message = decrypt(encrypted_message, rows)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
