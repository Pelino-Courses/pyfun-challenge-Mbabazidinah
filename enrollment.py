class Enrollment:
    def __init__(self, student, course):
        student.join_course(course)
        self.student = student
        self.course = course