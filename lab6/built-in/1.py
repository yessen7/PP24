def multiply_list(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result

my_numbers = [2, 3, 4, 5]
result = multiply_list(my_numbers)

print(f"The product of the numbers in the list is: {result}")

