students = []


# Simple function, if we want to set a default parameter we can put
# something like this "student_id=332"
def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    studens_titlecase = get_students_titlecase()
    print(studens_titlecase)


# We can send arguments like "Hello",3,None.
# We must to add *
def var_args(name, *args):
    print(name)
    print(args)  # We don't have tu add the * when the parameter args is used


def var_kwargs(name, **kwargs):  # We can use keyword arguments
    print(name)
    print(kwargs["description"])


add_student("Mark")  # We just send 'Mark' and the student_value will be 332 (default value)
add_student("Cesar", 223)  # The student_id will be 223
add_student(name="Mark", student_id=450)  # We can use "Named Arguments", it's very useful
var_args("Test", "Hola", "Cesarin", 3, None)
var_kwargs("Prueba2", description="keyword arguments", feedback=None, pluralsight="Yes")