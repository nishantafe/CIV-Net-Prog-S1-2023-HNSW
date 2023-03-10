def greet():
    print("Hello")


def get_name_and_greet():
    name = input("Enter your name: ")
    print("Hello", name)


def verify_age():
    age = int(input("Enter you age: "))
    if age >= 18:
        print("You're an adult.")
    else:
        print("You're a minor.")


def is_successful(result):
    if result >= 50:
        return True
    else:
        return False


def assess_result():
    my_result = int(input("Enter your result: "))
    if is_successful(my_result):
        print("You have been successful")
    else:
        print("You haven't been successful")


def multiplier(num1, num2):
    return num1 * num2


def convert_aud_to_usd(amount):
    conversion_rate = 0.66  # Local variable to the function
    return amount * conversion_rate


# print(conversion_rate) # This will return a NameError because it's a local variable

my_amount = 100  # Global variable, can be used anywhere, even in functions
print("USD", convert_aud_to_usd(my_amount))

# greet()
# get_name_and_greet()
# verify_age()
# print(is_successful(20))
# assess_result()
# print(multiplier(5, 5))
