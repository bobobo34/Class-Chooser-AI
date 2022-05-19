from classes import *
from namegenerator import gen

zepf = Teacher(
    createClasses("APWH", [2, 3, 4], 20),
    "Dan Zepf",
    2515
)
heile = Teacher(
    createClasses("English 1", [2, 3, 4], 20),
    "Elizabeth Heile",
    2534
)
mcg = Teacher(
    createClasses("Scriptures", [2, 3, 4], 20),
    "Kim McGlaughin",
    3544
)
brass = Teacher(
    createClasses("Drawing", [6], 20),
    "Eric Brass",
    2102
)
lavelle = Teacher(
    createClasses("Bio", [5, 6, 8], 20),
    "Stephen LaVelle",
    2565
)
brown = Teacher(
    createClasses("German", [2, 4, 7], 20),
    "Julia Brown",
    3530
)
nikias = Teacher(
    createClasses("Algebra 2", [1], 20),
    "Alex Nikias",
    1512
)
brower = Teacher(
    createClasses("Algebra 2", [5, 8], 20),
    "Jim Brower",
    1530
)
nardini = Teacher(
    createClasses("Bio", [1], 20),
    "Heather Nardini",
    2534
)

# NEED TO DO:
# IF OTHER CLASSES ARE FULL NEED TO CHANGE ONE OF CLASSES TO FIT BELLS

stX = School("St. Xavier High School", 8)
stX.add_teachers([zepf, heile, mcg, lavelle, nikias, brower, brass, brown])


for i in range(50):
    stX.add_students([Student(
        gen(),
        ["APWH", "English 1", "Scriptures", "Algebra 2", "German", "Drawing", "Bio"]
    )])

stX.give_classes()
stX.print_schedule()

for student in stX.students:
    print(len(student.scheduled_classes))
