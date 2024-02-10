import random


def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


grams_amount = 200
ounces_result = grams_to_ounces(grams_amount)
print(f"{grams_amount} grams is {ounces_result:.2f} ounces.")



def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


fahrenheit_temp = 451  # float(input("Enter Fahrenheit temperature: "))
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} degrees Fahrenheit is {celsius_temp:.2f} degrees Celsius.")



def solve(numheads, numlegs):
    legs_per_chicken = 2
    legs_per_rabbit = 4

    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = (num_chickens * legs_per_chicken) + (num_rabbits * legs_per_rabbit)
        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None


numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"There are {chickens} chickens and {rabbits} rabbits.")
else:
    print("No solution found.")



def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed sentence:", result)



def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))



def spy_game(nums):
    sequence_position = 0

    for num in nums:
        if num == 0 and sequence_position == 0:
            sequence_position += 1
        elif num == 0 and sequence_position == 1:
            sequence_position += 1
        elif num == 7 and sequence_position == 2:
            return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))   # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))   # Output: False



def volume(r):
    pi = 3.14
    area = pi*(r**2)
    return area


r = 10
print(volume(r))



def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", result_list)



def is_palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]


input_word = "Madam"
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")



def histogram(numbers):
    for num in numbers:
        print('*' * num)


histogram([4, 9, 7])



def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


guess_the_number()

