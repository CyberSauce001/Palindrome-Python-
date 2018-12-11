def is_palindrome(value):
    return len(value) < 2 or value[0] == value[-1] and is_palindrome(value[1:-1])

value = input('Enter a Palindrome: ')
print(is_palindrome(value))
