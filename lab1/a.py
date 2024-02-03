import random
# syntax
if 5 > 2:
    print("Five is great than two")

# this is a comment
print("Hello, World!") # this is a comment

# variables
x = 5
y = "John"
x = "Sally"
print(x)
print(y)
q = str(3)
w = int(3)
e = float(3)
print(type(q))
r = 'John'
X = 10

# variable names
my_var = "John"
myVariableName = "Alex"
MyVariableName = "Alexia"
my_variable_name = "Alexandra"

a, s, d = "Orange", "Banana", "Cherry"
print(a, s, d)
a = s = d = "Orange"
print(a, s, d)

fruits = ["apple", "banana", "cherry"]
a, s, d = fruits
print(a, s, d)

# output variables
x, y, z = "Python", "is", "awesome"
print(x, y, z)
print(x + y + z)
x, y = 5, 10
print(x + y)
y = "John"
# print(x+y)  # error
print(x, y)

# global variables
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc1():
    global x
    x = "fantastic"


myfunc1()
print("Python is " + x)

# variable exercises
car_name = "Volvo"

# data types
x = 5
print(type(5))
x = list(("apple", "banana", "cherry"))
y = tuple(("apple", "banana", "cherry"))
z = set(("apple", "banana", "cherry"))

# numbers
x = 1j
y = 2323
z = 10.01
print(type(x))
print(type(y))
print(type(z))

b = int(y)
c = complex(x)
print(type(b))
print(type(c))

print(random.randrange(1, 10))

# casting
x = float(1)

# strings
a = """Use three double quotes
to assign a multiline"""
print(a)
print(a[1])

for x in "banana":
    print(x)


print(len(a))
print("mul" in a)
if "mul" in a:
    print("Yes, 'mul' is present")


print("hello" not in a)
if "mul" not in a:
    print("No, 'mul' is NOT present")

# strings - slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

# string - modify
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

# string concatenation
a = "Hello"
b = "World"
c = a + b
d = a + " " + b
print(c)
print(d)

# string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item{1}"
print(my_order.format(quantity, itemno, price))

# string escape characters
txt = "We are so-called \"humans\" from the west"
print(txt)

# string methods
print(txt.capitalize())

# exercises
x = "Hello World"
print(len(x))
