import mymodule as mx
import platform
from mymodule import person1


# Modules - A file containing a set of functions you want to include in your application.
mx.greeting("Yessen") # mymodule.greeting("Yessen")

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)
y = dir(platform)
print(y)
