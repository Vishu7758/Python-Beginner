students = []


def print_student_name(name):
    print(name)


def add_student(name,id=1):
    student = {"name":name, "id":id}
    students.append(student)


print_student_name("Ashpreet")
#add_student("Deepu")
add_student("Deepu")
print(students)

print("Ashpreet","Deepu","Hello")