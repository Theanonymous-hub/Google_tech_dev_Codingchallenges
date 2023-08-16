'''Given an integer number n, return the difference between
the product of its digits and the sum of its digits.

Leetcode 1281 : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15 '''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product =1
        sum =0
        while n>0:
            digit =n%10
            product  *=digit
            sum +=digit
            n//=10
        return product-sum