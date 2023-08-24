'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''
def isValid(self, s: str) -> bool:
    st = []
    d = {"(": ")", "[": "]", "{": "}"}
    for i in s:
        if i in d.keys():
            st.append(i)
        else:
            if st == []:
                return 0
            else:
                if d[st[-1]] == i:
                    st.pop()
                else:
                    return 0
    if st == []:
        return 1
    else:
        return 0