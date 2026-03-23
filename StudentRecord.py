# Advanced Tuple Program

students = (
    ("Rahul", 85),
    ("Anita", 90),
    ("Amit", 78),
    ("Neha", 88)
)

print("Student Records")

for name, marks in students:
    print("Name:", name, "| Marks:", marks)

highest = 0
topper = ""

for name, marks in students:
    if marks > highest:
        highest = marks
        topper = name

print("Topper is:", topper, "with marks", highest)