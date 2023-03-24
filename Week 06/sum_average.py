numbers = [10, 20, 30, 40, 50, 60, 50, 80, 80, 80]
# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])
print("The sum of the numbers is:", sum(numbers))
print("The average of the numbers is:", sum(numbers) / len(numbers))

numbers.append(70)  # append() adds a new item to the list
print(numbers)
numbers.remove(20)  # remove() removes an exiting item from the list
print(numbers)
print(numbers.count(50))  # count() counts the amount of times an item is found in a list

print("50 is found", numbers.count(50), "time(s) in the list")
numbers.insert(2, 5)
print(numbers)
while 80 in numbers:
    numbers.remove(80)  # Get rid of all existences of 80 in the list
print(numbers)
