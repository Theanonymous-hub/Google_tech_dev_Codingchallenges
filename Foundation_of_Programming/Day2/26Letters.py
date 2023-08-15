'''Write a program which does the reverse of the example above:
it should take a character as input and output the corresponding number (between 1 and 26).
Your program should only accept capital letters.
As error-checking, print invalid if the input is not a capital letter.'''
try:
    char = input("Enter the character")

    if len(char) == 1 and 'A' <= char <= 'Z':
        number = ord(char) - ord('A') + 1
        print(number)
    else:
        print("invalid")
except ValueError:
    print("invalid")
