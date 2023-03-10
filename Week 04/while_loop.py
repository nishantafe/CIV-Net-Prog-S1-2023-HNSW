MENU = "l) Login, s) Sign up, q) Quit"
# MENU is in caps, and that means it's a CONSTANT
# The CONSTANT is like a variable, but it never changes its value

done = False
while not done:
    print(MENU)
    valid_username = "nishan"
    valid_password = "password"

    user_choice = input("Choose [l/s/q]: ")

    if user_choice == "l":
        print("Logging you in...")
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")
        if entered_username == valid_username and entered_password == valid_password:
            print("You have successfully logged in.")
        else:
            print("Invalid credentials.")
    elif user_choice == "s":
        print("Signing you up...")
    elif user_choice == "q":
        print("Quitting the program...")
        done = True  # stops the looping
    else:
        print("Invalid choice.")
