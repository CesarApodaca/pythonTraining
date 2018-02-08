student_names = ["James","Katarina","Jessica","Mark","Bort","Frank Grimes","Max Poxer"]

for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break
    print("Currently testing " + name)


# If we want to define a range, for example. Start from the second element,
# or increment by two unstead of 1. We can use the range function.

x = 0

for index in range(10):
    x += 10
    print("The value of X is {0}".format(x))

# We can set more parameters the start point, the end point and how many times you want to increase it
for index in range(2, 4, 1):
    print(student_names[index])
