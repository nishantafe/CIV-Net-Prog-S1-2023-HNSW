"""
Login [l]
Register [r]
    Generate password [y]
        Digits? [y]
        Symbols? [y]
        Length of password (default is 10) [50]
    Custom Password
View Accounts [v]
Exit [e]
"""
import random
import string
import time

FILE = "accounts.txt"
accounts_dictionary = {}


def read_file_into_dictionary(file, a_dictionary):
    file_in = open(file, "r")
    for line in file_in:
        username, password = line.split(" ")
        a_dictionary[username] = password.rstrip()
    file_in.close()


read_file_into_dictionary(FILE, accounts_dictionary)

print(accounts_dictionary)

# Check if a username exists
entered_username = input("Enter a username: ")
if entered_username in accounts_dictionary:
    print("Username found")
else:
    print("Username not found")

entered_password = input("Enter a password: ")
if entered_password == accounts_dictionary[entered_username]:
    print("You entered", entered_password)
    print("and it matches:", accounts_dictionary[entered_username])
else:
    print("Invalid password for", entered_username)


def view_accounts():
    print(f"{'Username':13s} Password\n--------------------")
    for a_username, a_password in accounts_dictionary.items():
        print(f"{a_username:13s} {a_password}")


# View accounts
view_accounts()

letters = string.ascii_letters  # Alphabet letter (upper & lower case)
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols

secret_word = ""
character_combo = letters
include_digits = input("Would you like to include digits? [y/n]: ").lower()
if include_digits == "y":
    character_combo += digits
secret_word_length = input("Enter the length (press enter for 10): ")
if secret_word_length == "":
    secret_word_length = 10
else:
    secret_word_length = int(secret_word_length)

for character in range(secret_word_length):
    secret_word += random.choice(character_combo)
# print(secret_word)

# Save
new_username = input("Enter a new username: ")
new_password = input("Enter a new password: ")
accounts_file_out = open(FILE, "a")
accounts_file_out.write(new_username + " " + new_password + "\n")
accounts_file_out.close()

print("Exiting...")
time.sleep(2)


