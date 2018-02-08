from P3ObjectedOrientedProgramming.student import Student


class HighSchoolStudent(Student):

    school_name = "Springfield"

    def get_school_name(self):
        return "This is a High School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "~HS"
