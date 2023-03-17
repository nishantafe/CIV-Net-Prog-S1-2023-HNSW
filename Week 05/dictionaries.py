my_dictionary = {"John": "0456454222", "Sara": "0456532259", "Jonathan": "0455782236"}

# Get the keys of a dictionary
print(my_dictionary.keys())

# Get the values of a dictionary
print(my_dictionary.values())

# Get the items (pairs) of a dictionary
print(my_dictionary.items())

# Get the value of a specific key in the dictionary
print(my_dictionary["Sara"])

# Challenge: Get John's phone number from the dictionary
print("John's phone number is:", my_dictionary["John"])

# Add a new item (pair) to the dictionary
my_dictionary["Joe"] = "0423569999"
print(my_dictionary)

# Use a for loop with .items() to neatly display keys and values in a dictionary
for one_key, one_value in my_dictionary.items():
    print(one_key, one_value)
