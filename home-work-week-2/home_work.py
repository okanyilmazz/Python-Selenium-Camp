students=[]

def get_full_name():
    first_name = input("Please enter the first name ")
    last_name = input("Please enter the last name ")
    if(first_name.isalpha() and last_name.isalpha()):
        return (first_name + " " + last_name)
    else :
        print("Attention! Please re-enter student information")
        get_full_name()

def add_student():
    full_name = get_full_name()
    students.append(full_name)

def remove_student():
    full_name = get_full_name()
    if(full_name in students):
        students.remove(full_name)
        print("Student has been deleted")
    else:
        print("Student does not exist")

def add_students():
    student_count = input("Please enter the number of students to be added ")
    if(student_count.isnumeric()):
        for i in range(0,int(student_count)):
            add_student()
    else:
        print("Attention! Please re-enter number")
        add_students()


def get_students():
    for student in students:
        print(student)

def get_students_number():
    for student in students:
        student_number=students.index(student)
        print(str(student_number+1) + " - " + student)

def remove_students():
    student_count = input("Please enter the number of students to be deleted ")
    if(student_count.isnumeric()):
        i=0
        while i<int(student_count):
            remove_student()
            i=i+1
    else:
        print("Attention! Please re-enter number")
        remove_students()

print(" -- Add Student -- ")

# add_student()
# get_students()

print(" -- Remove Student -- ")

# remove_student()
# get_students()

print(" -- Add Students -- ")

add_students()
# get_students()

# print(" -- Get All Students -- ")
# get_students()

print(" -- Get Students With Number -- ")
get_students_number()


print(" -- Remove Students -- ")
remove_students()
get_students_number()
