# LAB2
# boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 3
if b < a:
    print("b is greater than 2")
else:
    print("b is NOT greater than 2")


print(bool("Hello"))
print(bool(15))

bool(123)
print(bool(False))
print(bool(None))
print(123)
print(bool(""))
print(bool(), "\n")


class myClass():
    def __len__(self):
        return 0;


myObj = myClass()
print(bool(myObj))

def myFunction():
    return True


print(myFunction())


def myFunction1():
    return True


if myFunction1():
    print("YES!")
else:
    print("NO!")


x = 200
print(isinstance(x, int))

print(10 > 9)  # True

# operators
print(10 + 5)
print(100 + 5 * 3)  # multiplying is first
print(10*3)  # answer is 30

# lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
mylist = ["apple", "banana", "cherry", "cherry", "cherry"]
print(mylist)

print(len(mylist))
list1 = [1, 5, 9, 3]
list2 = ["abc", 5.1, True, 3]
print(type(list2))

thislist = list((1, 2, 3))
print(thislist)

# list - access list items
list10 = ["apple", "banana", "cherry"]
print(list10[1])
print(list10[1:2])

if "apple" in list10:
    print("Yes, \"apple\" is in the fruits list")

# list - change list items
print(list10)
list10[0] = "orange"
print(list10)
list10.insert(2, "watermelon")
print(list10)

# list - append items
list10.append("kiwi")
print(list10)

trop = ["mango", "pineapple", "papaya"]
list10.extend(trop)
print(list10)

list20 = ["tomato", "cucumber"]
trop = ("kiwi", "orange")
list20.extend(trop)
print(list20)

# list - remove list items
list20.remove("cucumber")
print(list20)
list20.pop(2)

del thislist
list10.clear()

# loop list
for x in list20:
    print(x)


for i in range(len(list20)):
    print(list20[i])


i = 0
while i < len(list20):
    print(list20)
    i = i + 1


# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)


print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

# sort list
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.sort(key=str.upper)
print(fruits)
fruits.reverse()
print(fruits)

# copy list
yourlist = fruits.copy()
yourlist = list(fruits)

# join two lists
list3 = fruits + yourlist
print(list3)

# exercise
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ["apple", "banana", "cherry"]
print("\n")

# tuples
mytuple = ("apple", "banana", "cherry")
print(mytuple)
thistuple = ("apple",)
print(type(thistuple))

# tuples - update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

z = ("hi", "hello", "bye")
w = list(z)
w.append("see you")
z = tuple(w)
print(z)

# tuples - unpack tuples
(green, yellow, red, blue) = z
print(green)

print(z.count("hi"))

# exercises
fruits = ("apple", "banana", "cherry")
print(fruits)  # ("apple", "banana", "cherry")

# sets
myset = {"apple", "banana", "cherry"}
print(myset)

for x in myset:
    print(x)

myset.add("orange")

tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)

myset.remove("pineapple")  # you can use set.discard(), it's not causing the error

tropical.pop()
tropical.clear()
myset3 = myset.union(tropical)

# exercises
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("yes, it's there")


# dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
x = thisdict.keys()
z = thisdict.values()
print(x, "\n", z)
thisdict["color"] = "red"
print(x)
thisdict["year"] = 2000
print(z)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
for x in thisdict.items():
    print(x)

# nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
thisdict["model"] = "Meow"

# exercises
print(thisdict.get("model"))

# if...else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# while loops
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


