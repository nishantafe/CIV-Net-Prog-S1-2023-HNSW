"""This program will detect any capital letter in a
word entered by the user and display a message"""

word = input("Enter a word: ")
caps_count = 0

# For loop to count the caps in the word
for letter in word:
    if letter == letter.upper() and letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        caps_count += 1

if caps_count > 0:
    print("Found", caps_count, "capital letter(s)")
else:
    print("No capital letters were found")
