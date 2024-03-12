def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()

    return cleaned_string == cleaned_string[::-1]


user_input = ""

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

