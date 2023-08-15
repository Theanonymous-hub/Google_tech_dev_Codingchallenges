''' First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320
https://www.coderbyte.com/editor/First%20Factorial:Python3'''

def FirstFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial
user_input = int(input())
if 1 <= user_input <= 18:
    result = FirstFactorial(user_input)
    print(result)