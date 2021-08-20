################################ Example 1 ######################################
# self keyword is always required
# -> it is a reference to the object (instance) of the class that we create (init) or
#    on which we call a method on (bark)
#   -> 'self' points to the object itself
#      -> the object (represented by self) gets passed as an argument when a function is called uppon it
class Dog:

    # constuctor
    def __init__(self, name, age):
        self.name = name                  # this is a new attribute of class dog!
        self.age = age

    # method in the object class
    def bark(self):
        print("bark")

    def getAge(self):
        return self.age

    # set age to a new value
    def setAge(self, age):
        self.age = age

# create dog objects
d = Dog("Timo", 3)
print(d.name)
print(d.getAge())
d.setAge(4)
print(d.age)
# call function on that object
d.bark()

############################ Example 2 ###############################
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return(self.grade)


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []                     # list of student object

    def add_student(self, student):
        if len(self.students) <= self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_grade_avg(self):
        mean = 0
        for st in self.students:
            mean += st.get_grade()
        return mean/len(self.students)


#################################### Example 3 ################################
# inheritance
# - we have a super calss 'pet' that inherits to the sub classes bird and cat

# super class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

# inheritance is enforced by putting the name of the superclass in the perenthesis of the sub class
class Bird(Pet):
    # no need to call the super costructor!

    def speak(self):
        print('piep')

# if Cat should have attributes that are not in the Pet class we can make a new constructor vor Cat
# We can call 'super' to call the constructor of the super class Pet
class Cat(Pet):
    # this is a static attribute which is the same for all members of the class
    # it can be calles via evry instance of the class, or via Cat.is_living
    # this is a good way to avoid global variables. In this way, the static variable will be still acessable when we
    # import the class in a new file
    is_living = True
    # GRAVITY will now be accessable even in a nother file!
    GRAVITY = -9.8
    number_of_cats = 0

    def __init__(self, name, age, claws):
        # let the super constructor inistiate the inherited attributes
        super().__init__(name, age)
        # and this is the part of the sub class consturctor
        self.claws = claws
        Cat.add_cat()

    def speak(self):
        print('mieow')

    """class methods 
    - class methods can only access class attributes
    - they cannot access the attribute of an instance of a class (object)
    - they are marked by the @classmethod key word"""
    @classmethod
    def add_cat(cls):
        cls.number_of_cats += 1


###################################### Example 5 #######################################
"""static methods
- methods in a class which do not change anything in the class
- they don't need a 'self' keyword
- they help to organise code which than can be imported with the 'import' key word
"""
class My_math:

    @staticmethod
    def add_one(x):
        return x + 1



if __name__ == '__main__':
    # example 2
    course1 = Course("info", 20)
    student1 = Student("Tim", 15, 75)
    student2 = Student("Lars", 16, 80)
    student3 = Student("Kathrin", 15, 85)

    # add students to course
    course1.add_student(student1)
    course1.add_student(student2)
    course1.add_student(student3)
    print(course1.students)
    print(course1.get_grade_avg())

    # example 3
    p = Pet('Bill', 30)
    p.show()
    c = Cat('Hula', 23, True)
    c.show()
    print(c.is_living)
    print(Cat.is_living)
