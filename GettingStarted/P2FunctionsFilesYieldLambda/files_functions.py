# "w" - Writing; overwrites the entire file
# "r" - reading a text file
# "a" - appending to a new or existing file
# "rb" - reading a binary file
# "wb" - writing to a binary file


students = []


# Simple function, if we want to set a default parameter we can put
# something like this "student_id=332"
def add_student(name, student_id="332"):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    studens_titlecase = get_students_titlecase()
    print(studens_titlecase)


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_idt = input("Enter student id: ")

add_student(student_name, student_idt)
save_file(student_name)