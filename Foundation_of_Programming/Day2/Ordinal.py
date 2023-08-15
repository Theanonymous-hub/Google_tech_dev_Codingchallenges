''' The words 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th are called ordinal adjectives.
Write a program which reads an integer x between 1 and 9 from input.
The program should output the ordinal adjective corresponding to x.
Hint: you don't need to have 9 separate cases; 4 is enough.'''
x=int(input())
if 1 <= x <= 9:
            if x == 1:
                ordinal = "1st"
            elif x == 2:
                ordinal = "2nd"
            elif x == 3:
                ordinal = "3rd"
            else:
                ordinal = str(x) + "th"
            print(ordinal)