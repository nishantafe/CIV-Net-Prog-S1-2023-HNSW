"""
LBYL: Look before you leap
EAFP: Easier to ask for forgiveness than permission
"""
try:
    print(name)
except NameError:
    print("Sorry, the variable 'name' does not have a value yet.")

try:
    number = input("Enter a number: ")
    number = int(number)
    print(number)
except ValueError:
    print("Invalid number.")

