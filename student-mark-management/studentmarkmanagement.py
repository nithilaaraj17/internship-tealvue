
students = []

subjects = ("python", "java", "maths")

student_names = set()


# 1. Add Student
def add_student():
    name = input("Enter the student name: ")

    if name in student_names:
        print("Student already exists")
        return

    python = int(input("Enter the python marks: "))
    java = int(input("Enter the java marks: "))
    maths = int(input("Enter the maths mark: "))

    student = {
        "name": name,
        "marks": [python, java, maths]
    }

    students.append(student)
    student_names.add(name)

    print("Student added successfully")


# 2. Display Students
def display_student():
    if len(students) == 0:
        print("No students found")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Python:", student["marks"][0])
        print("Java:", student["marks"][1])
        print("Maths:", student["marks"][2])


# 3. Search Student
def search_student():
    name = input("Enter the name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Python:", student["marks"][0])
            print("Java:", student["marks"][1])
            print("Maths:", student["marks"][2])
            return

    print("Student not found")


# 4. Update Marks
def update_mark():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            python = int(input("Enter the new python marks: "))
            java = int(input("Enter the new java mark: "))
            maths = int(input("Enter the new maths mark: "))

            student["marks"] = [python, java, maths]

            print("Marks updated successfully")
            return

    print("Student not found")


# 5. Delete Student
def delete_student():
    name = input("Enter the student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():

            students.remove(student)
            student_names.remove(student["name"])

            print("Student deleted successfully")
            return

    print("Student not found")



def calculate_total():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            total = sum(student["marks"])

            print("Total marks =", total)
            return total

    print("Student not found")
    return 0



def calculate_average():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            total = sum(student["marks"])
            average = total / len(student["marks"])

            print("Average =", average)
            return average

    print("Student not found")
    return 0



def highest_mark():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            highest = max(student["marks"])

            print("Highest mark =", highest)
            return highest

    print("Student not found")
    return 0



def lowest_mark():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            lowest = min(student["marks"])

            print("Lowest mark =", lowest)
            return lowest

    print("Student not found")
    return 0



def check_Result():
    name = input("Enter the student name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            marks = student["marks"]

            if all(mark >= 40 for mark in marks):
                print("Result: PASS")
            else:
                print("Result: FAIL")

            return

    print("Student not found")
def display_subjects():
    print("Subjects:")

    for subject in subjects:
        print(subject)



while True:

    
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Total")
    print("7. Calculate Average")
    print("8. Highest Mark")
    print("9. Lowest Mark")
    print("10. Check Pass/Fail")
    print("11. Display Subjects")
    print("12. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_mark()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        calculate_total()

    elif choice == 7:
        calculate_average()

    elif choice == 8:
        highest_mark()

    elif choice == 9:
        lowest_mark()

    elif choice == 10:
        check_Result()

    elif choice == 11:
        display_subjects()

    elif choice == 12:
        print("Program ended")
        break

    else:
        print("Invalid choice")
