from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "TA"