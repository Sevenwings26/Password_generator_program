# program that will generate passwords for users - PyPassword Generator.
letters = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

n_letters = int(input('How many letters would you like in your passwors? \n'))
print('\n')

n_symbols = int(input("How many symbols would you like? \n"))
print('\n')

n_numbers = int(input("How many numbers would you like? \n"))

import random
# Easy level 

# Pick at random more than one characters
random_letters = random.sample(letters, n_letters)
random_numbers = random.sample(numbers, n_numbers)
random_symbols = random.sample(symbols, n_symbols)
# extend lists
random_letters.extend(random_symbols)
random_letters.extend(random_numbers)
password = random_letters
print('\n')
# join list items together
finalpassword = ''.join([str(char) for char in password])
print(type(finalpassword))
print(f"Here is your password: {finalpassword}")



# # Hard approach 
# random.shuffle(password)
# finalpassword = ''.join([str(char) for char in password])
# print(f"Here is your password: {finalpassword}")
# print('\n')

# # program that will generate passwords for users - PyPassword Generator.
# letters = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")

# n_letters = int(input('How many letters would you like in your passwors? \n'))
# print('\n')

# n_symbols = int(input("How many symbols would you like? \n"))
# print('\n')

# n_numbers = int(input("How many numbers would you like? \n"))

# import random

# password = " "

# for char in range(1, n_letters + 1):
#     random_letters = random.choice(letters)
#     password += random_letters
# for char in range(1, n_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, n_numbers + 1):
#     password += random.choice(numbers)

# print(f"password: {password}")
