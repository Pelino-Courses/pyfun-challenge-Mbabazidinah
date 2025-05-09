from person import Person

class Instructor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_role(self):
        return "Instructor"
