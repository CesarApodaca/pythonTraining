student_names = ["Mark", "Katarina", "Jessica"]
student_list = []   # without items
print(student_names[0])
print(student_names[2])

# If we want to add more elements to our list, we can use that:

student_names.append("Cesarin")
print(student_names)

# If we want to verify if an elements exists, we use this:
print("Cesarin" in student_names)   # it returns True

# If we want to know how many items we have, we use this:
print(len(student_names))   # It returns 4 elements

# If we want to remove an element from our list we use this:
del(student_names[3])   # It removes the last item "Cesarin"
print(student_names)

print(student_names[-1])    # It prints the last item


# If we want tu print our list, we can use a loop
student_names = ["James","Katarina","Jessica","Mark","Bort","Frank Grimes","Max Poxer"]

for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break
    print("Currently testing " + name)

print(len(student_names))