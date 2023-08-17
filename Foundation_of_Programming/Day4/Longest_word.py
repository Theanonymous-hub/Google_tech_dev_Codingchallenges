import re

def LongestWord(sen):
    words = re.findall(r'\w+', sen)  # Extract words using regular expression
    longest_word = max(words, key=len)  # Find the longest word using the length as the key
    return longest_word

# Keep this function call here
print(LongestWord(input()))
