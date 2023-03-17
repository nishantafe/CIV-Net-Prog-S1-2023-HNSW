import random
import string
import time

random_number = random.randint(1, 10)
print(random_number)

letters = string.ascii_letters  # Alphabet letter (upper & lower case)
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)

# With random.choice(source) you can get 1 choice from the source data
random_letter = random.choice(letters)
random_digit = random.choice(digits)
random_symbol = random.choice(symbols)

print("Random letter:", random_letter)
print("Random digit:", random_digit)
print("Random symbol:", random_symbol)

character_limit = 50
my_magical_word = ""
for character in range(character_limit):
    my_magical_word += random.choice(letters + digits + symbols)
print("My magical word is:", my_magical_word)

print(f"A message will be displayed in 3 seconds...")
time.sleep(3)
print("The 3 seconds are over. Thanks you!")

print("Processing...")
for i in range(10):
    time.sleep(1)
    print(f"\r{i * 10 + 10}%", end="")
print("\nComplete!")
