"""Force someone to say Yes!"""

answer = input("Yes or no: ").lower()

while answer != "yes":
    answer = input("Yes or no: ").lower()

print("Thanks you!!!")
