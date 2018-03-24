print("Hello World")


# Strings

fname = "Ashpreet"
lname = "Saluja"
print(fname+" "+lname)

name = "Ashpreet"
machine = "Hal"
print("Nice to meet you {0}.I am {1}".format(name, machine))


# Boolean

flag = True
print(int(flag))

# if statements

number = 5
if number == 5:
    print("Executed")
    print("Entered if")
else:
    print("Not executed")

a = 1
b = 2
print("bigger" if a > b else "smaller")


# Lists

persons = ["Ash", "Ashish", "Raghav"]
print(persons[0])
del persons[2]
print(persons)

persons.append("Deepu")
print(persons)

print(persons[1:])
print(persons[0:1])


# For loop functionality
for name in range(len(persons)):
    print(persons[name], end=" ")
