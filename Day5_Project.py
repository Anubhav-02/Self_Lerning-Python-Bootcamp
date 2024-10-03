import random

print("Welcome to the Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '?']

# Get the number of letters, numbers, and symbols from the user
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

# Create an empty list to store the password characters
password_list = []

# Add random letters to the password list
for _ in range(num_letters):
    password_list.append(random.choice(letters))

# Add random numbers to the password list
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols to the password list
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Join the list into a string to form the final password
password = ''.join(password_list)

print(f"Your generated password is: {password}")
