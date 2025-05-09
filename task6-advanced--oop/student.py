from person import Person

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.my_courses = []

    def join_course(self, course):
        self.my_courses.append(course)
        course.add_student(self)

    def __iter__(self):
        return iter(self.my_courses)

    def get_role(self):
        return "Student"
