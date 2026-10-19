from student import Student
from faculty import Faculty
from person import Person

stu1 = Student('Johnny', 21, 'blonde', ['CIT260', 'CIT123', 'CSC124'])
fac1 = Faculty('Anne', 42, 'black', 70000)

print(stu1.get_name())
print(fac1.get_name())

stu1.age = -50

print(stu1.age)