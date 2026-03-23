# Advanced Dictionary Program

students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show All Students")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter student name to delete: ")
        students.pop(name, "Student not found")

    elif choice == 4:
        print("Student List:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 5:
        break

    else:
        print("Invalid choice")