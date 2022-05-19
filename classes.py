from dataclasses import dataclass
import random
from collections import Counter
from itertools import repeat, chain


@dataclass
class Student:
    name: str
    ideal_classes: list[str]
    def __post_init__(self):
        self.school: School = None
        self.scheduled_classes: list = []
        self.teachers: list[str] = []
    def __repr__(self) -> str:
        return f"{self.name} ({self.school.name}), teachers: {self.teachers}"

@dataclass
class Class:
    name: str
    bell: int
    capacity: int
    def __post_init__(self):
        self.students: list[Student] = []
        self.full = False
    def __repr__(self):
        return f"{self.name}"
    def add_student(self, student: Student):
        if len(self.students) == self.capacity - 1:
            self.full = True
            #raise Exception("This class is full!")
        self.students.append(student)
        
def createClasses(name: str, bells: list[int], capacity) -> list[Class]:
    return [Class(name, bell, capacity) for bell in bells]

@dataclass
class Teacher:
    classes: list[Class]
    name: str
    room: int
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.room})"
    def get_taught_classes(self):
        return [(c.name, c.bell, c) for c in self.classes if not c.full]
    
    
        
        
@dataclass
class School:
    name: str
    bells: int
    def __post_init__(self):
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.classes: set[str] = set()
    def __repr__(self):
        val = f"{self.name}\nBells: {self.bells} \nStudents:\n"
        for student in self.students:
            val += f"\t{student}\n"
        val += "Teachers:\n"
        for teacher in self.teachers:
            val += f"\t{teacher}\n"
        return val
    def add_students(self, students: list[Student]):
        for student in students:
            for clas in student.ideal_classes:
                if clas not in self.classes:
                    raise NoClassError(clas) 
            self.students.append(student)
            student.school = self
    def add_teachers(self, teachers: list[Teacher]):
        for teacher in teachers:
            self.teachers.append(teacher)
            for clas in teacher.classes:
                self.classes.add(clas.name)
    def get_classes(self, classes: list[str], given_classes: list=[]):
        #example classes: [APWH, English 1, Scriptures]
        chosen_classes = []
        total_classes = []
        for teacher in self.teachers:
            for clas in teacher.get_taught_classes():
                total_classes.append((clas[0], clas[1], teacher.name, clas[2]))
        #get rid of unnecessary classes
        total_classes = [clas for clas in total_classes if clas[0] in classes]
        total_dupe = total_classes

        #get rid of given classes
        #print("OG GIVEN:", given_classes)
        for cla in given_classes: 
            #print(cla, type(cla))
            chosen_classes.append((cla[0].name, cla[0].bell, cla[1], cla[0]))
            total_classes = [clas for clas in total_classes if clas[0] is not cla[0].name and clas[1] is not cla[0].bell]
            #print("NEW TOTAL: ", total_classes)

        #get least common
        while(total_classes):
           
            names = [c[0] for c in total_classes]
            least_common_name = Counter(names).most_common()[-1][0]
            #print(least_common_name)
            classes_with_name = [c for c in total_classes if c[0] is least_common_name]
            random_classes_w_name = random.sample(classes_with_name, len(classes_with_name))
            chosen_class = random_classes_w_name[0]
            #print(type(chosen_class), chosen_class)
            chosen_classes.append(chosen_class)
            total_classes = [clas for clas in total_classes if clas[0] is not least_common_name and clas[1] is not chosen_class[1]]
        #example classes: [(apwh, 2), (scrip, 2)]
        #example bells: (2, 3, 4)
        not_chosen = list_minus(classes, [c[0] for c in chosen_classes])
        #print(not_chosen)
    
        last_classes: list = [c for c in total_dupe if c[0] in not_chosen]
        #print(last_classes)
        for c in last_classes:
            
            if not c[3].full:
                
                given_classes.append((c[3], c[2]))
                #print("classes available!")
                print("NEW GIVEN", given_classes)
                return self.get_classes(classes)

        #print("\n")

        return chosen_classes


        
    #organize classes for all students
    def give_classes(self):
        
        random_students: list[Student] = random.sample(self.students, len(self.students))
        #random_teachers: list[Teacher] = random.sample(self.teachers, len(self.teachers))
        for student in random_students:
            # for clas in student.ideal_classes:
            #     for teacher in random_teachers:
            #         if clas in teacher.get_taught_classes():
            #             for c in teacher.classes:
            #                 try:
            #                     bells = [c[2] for c in student.scheduled_classes]
            #                     if c.bell in bells:
            #                         continue
                                
            #                     c.add_student(student)
            #                     student.scheduled_classes.append((teacher.name, c, c.bell))
            #                     break
            #                 except Exception:
            #                     pass
            classes = self.get_classes(student.ideal_classes)
            
            for clas in classes:
                clas[3].add_student(student)
                student.scheduled_classes.append((clas[0], clas[1], clas[2]))
    def print_schedule(self):
        for student in self.students:
            print(f"{student.name}:\n")
            for clas in student.scheduled_classes:
                print(f"\t{clas}\n")

                        
#other way to do: get all classes and available bells, then assign one to each

def list_minus(lst1, lst2): 
    lst3 = [value for value in lst1 if value not in lst2] 
    return lst3 
                
class NoClassError(Exception):
    def __init__(self, clas:str=None, message="Your school doesn't have this class!"):
        self.message = message
        if clas:
            self.message = f"Your school doesn't have {clas}!"
        super().__init__(self.message)




# zepf = Teacher(
#     createClasses("APWH", [2, 3, 4], 20),
#     "Dan Zepf",
#     2515
# )
# heile = Teacher(
#     createClasses("English 1", [2, 3, 4], 2),
#     "Elizabeth Heile",
#     2534
# )
# evin = Student(
#     "evin",
#     ["APWH", "English 1"]
# )
# eli = Student(
#     "eli",
#     ["APWH", "English 1"]
# )
# vincent = Student(
#     "vincent",
#     ["English 1"]
# )

# stX = School("St. Xavier High School", 8)
# stX.add_teachers([zepf, heile])
# stX.add_students([evin, eli, vincent])
# print(stX)
# stX.give_classes()
# print(evin.scheduled_classes)
# print(eli.scheduled_classes)
# print(vincent.scheduled_classes)
