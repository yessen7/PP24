# functions

def my_function(fname, lname):
    print(fname + " " + lname)


print(my_function("Yessen", "Otegen"))


def my_function1(x):
    return 5 * x


print(my_function1(3))



# lambda
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def myfunc(n):
    return lambda a : a * n


mytripler = myfunc(3)

print(mytripler(100))


# classes/objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Student(Person):
    pass


x = Student("Yeso", 19)
x.print_age()



class Master(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.name, "who graduated in", self.graduation_year)


x = Master("Yeso", "Otegen", 2020)
x.welcome()

