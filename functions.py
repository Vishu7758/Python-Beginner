students = []


def print_student_name(name):
    print(name)


def add_student(name,id=1):
    student = {"name":name, "id":id}
    students.append(student)


def var_args(name,*args):
    print(name)
    print(args)

def key_var_args(name,**kwargs):
    print(name)
    print(kwargs["description"])


print_student_name("Ashpreet")
#add_student("Deepu")
add_student("Deepu")
print(students)

print("Ashpreet","Deepu","Hello")

var_args("Hello","Ashpreet","Ashish")

key_var_args("Ashpreet",description = "Loves food")