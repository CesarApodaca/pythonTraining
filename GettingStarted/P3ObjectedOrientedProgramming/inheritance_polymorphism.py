students = []


class Student:

    school_name = "Springfield"

    def __init__(self, name, student_id="332"):  # __init__ it's our constructor
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):  # we can customize our print
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):

    school_name = "Springfield"

    def get_school_name(self):
        return "This is a High School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "~HS"


james = HighSchoolStudent("James")
print(james.get_name_capitalize())


# in Python there are not access modifiers, Python doesn't have private, public or protected
# Python developers use the underscore prefix for a method name to denote that method
# Should not be overridden or even used directly.
