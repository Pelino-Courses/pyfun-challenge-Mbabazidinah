class Course:
    def __init__(self, name):
        if not name:
            raise ValueError("Course name required")
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return iter(self.students)

    def __add__(self, other):
        joined = Course(self.name + " & " + other.name)
        joined.students = self.students + other.students
        return joined

