# Homework 8 - Problem 6
# Polybius Checkerboard

def find_letter(board, letter):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == letter:
                return row, column

    return -1, -1


def encrypt(message):
    encrypted = ""

    for letter in message:
        row, column = find_letter(board, letter)

        if row != -1:
            encrypted += str(row) + str(column) + " "

    return encrypted.strip()


def decrypt(message):
    decrypted = ""
    numbers = message.split()

    for number in numbers:
        row = int(number[0])
        column = int(number[1])
        decrypted += board[row][column]

    return decrypted


# Create the checkerboard
board = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y", "Z"]
]

message = input("Enter a message: ").upper()
message = message.replace(" ", "")

encrypted_message = encrypt(message)
decrypted_message = decrypt(encrypted_message)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
