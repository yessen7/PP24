# Create a generator that generates the squares of numbers up to some number N.
#
# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
#
# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
#
# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
#
# Implement a generator that returns all numbers from (n) down to 0.


n = int(input("Enter n: "))


def even_generator(n):
    for num in range(0, n+1, 2):
        yield num


def square(n):
    for num in range(0, n+1):
        yield num**2


def divisible_to_3_and_4(n):
    for num in range(0, n+1):
        if((num%3) == 0) and ((num%4) == 0):
            yield num


def square_2(a, b):
    for num in range(a, b+1):
        yield num**2


def down_to_0(n):
    while n > -1:
        num = n
        yield num
        n -= 1


even_numbers = even_generator(n)
print("Even numbers: ")
for i in even_numbers:
    print(i)

square_numbers = square(n)
print("Square numbers: ")
for j in square_numbers:
    print(j)


d_3_4 = divisible_to_3_and_4(n)
print("Numbers divided to 3 and 4: ")
for k in d_3_4:
    print(k)


a = int(input())
b = int(input())

square_numbers_2 = square_2(a, b)
print("Square numbers from ", a, "to ", b)
for g in square_numbers_2:
    print(g)

to_0 = down_to_0(n)
print("From N to 0: ")
for v in to_0:
    print(v)

