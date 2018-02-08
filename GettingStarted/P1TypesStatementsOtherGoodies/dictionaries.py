# Dictionaries allow me to store key value pairs of any data easily

student = {
    "name": "Mark",
    "student_id": 123456,
    "feedback": None
}

print(student["name"] + " " + str(student["student_id"]))

# We can add/remove or modify our dictionary items with these lines of code

student["name"] = "Cesar"   # the name changes from Mark to Cesar

# We can see how many keys we have in our dictionary
student.keys()

# We can see our dictionary values with the values function
student.values()

# If we want to delete a key from our dictionary, we can use this function
del student["name"]  # without parenthesis
