from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course

s1 = Student("Alice")
s2 = Student("Bob")
i1 = Instructor("Dr. Smith")
ta = TeachingAssistant("Charlie")

c1 = Course("Physics")
c2 = Course("History")

s1.join_course(c1)
s2.join_course(c2)
i1.assign_course(c1)
ta.join_course(c1)
ta.assign_course(c2)

mix_course = c1 + c2

print("In mix course:")
for stu in mix_course:
    print(stu.name)

print(f"{s1.name}'s courses:")
for course in s1:
    print(course.name)

