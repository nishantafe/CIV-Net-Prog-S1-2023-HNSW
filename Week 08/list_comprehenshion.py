cars = ["Mercedes", "Volvo", "Ferrari", "Mazda"]
cars.append("Toyota")
print("Cars:", cars)

favourite_cars = []
for car in cars:
    if "r" in car:
        favourite_cars.append(car)
print("Favourite Cars:", favourite_cars)

# List comprehension
# The purpose is to create a list!

# list = [APPENDING ZONE    LOOPING ZONE]
best_cars = [car for car in cars]
print("Best cars:", best_cars)

# list = [APPENDING ZONE    LOOPING ZONE    IF CONDITION]
best_cars1 = [car for car in cars if "r" in car]
print("Best cars1:", best_cars1)

# list = [APPENDING ZONE    IF CONDITION WITH ELSE  LOOPING ZONE]
best_cars2 = ["good" if "r" in car else "bad" for car in cars]
print("Best cars2:", best_cars2)
print(best_cars1[0], best_cars2[0])
print(best_cars1[1], best_cars2[1])

# TODO: Create a list of results Pass/Fail based on grades in a list
# Condition to pass is the grade to be 50 or above
# The output should look ['Fail', 'Fail', 'Pass', 'Fail', 'Fail', 'Pass']

grades = [22, 44, 66, 34, 12, 99]
results = ["Pass" if grade >= 50 else "Fail" for grade in grades]
print("Results:", results)

