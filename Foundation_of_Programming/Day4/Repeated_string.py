'''Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
Given an integer, , find and print the number of letter a 's in the first letters of Lilah's infinite string.
Input Format
The first line contains a single string, .
The second line contains an integer, .
Constraints
For of the test cases, .
Output Format
Print a single integer denoting the number of letter a 's in the first letters of the infinite string created by
repeating infinitely many times.'''
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'repeatedString' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a_count_in_s = s.count('a')
    repetitions = n // len(s)
    remaining_chars = n % len(s)
    total_a_count = a_count_in_s * repetitions + s[:remaining_chars].count('a')
    return total_a_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

