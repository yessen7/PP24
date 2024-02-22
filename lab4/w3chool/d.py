


# Iterators - An iterator is an object that contains a countable number of values.
#
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter1 = iter(myclass)

print(next(myiter1))
print(next(myiter1))


# Scope - A variable is only available from inside the region it is created. This is called scope.
def myfunc():
    x = 200
    print(x)

myfunc()

x = 300
def myfunc2():
    print(x)

myfunc2()

def myfunc3():
    global y
    y = 100

myfunc3()
print(y)
