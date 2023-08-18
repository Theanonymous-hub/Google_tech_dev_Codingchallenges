'''Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10 '''


def FindIntersection(strArr):
    # Split the two comma-separated strings into lists of integers
    list1 = [int(x) for x in strArr[0].split(', ')]
    list2 = [int(x) for x in strArr[1].split(', ')]

    # Find the intersection of the two lists
    intersection = [str(num) for num in list1 if num in list2]

    if not intersection:
        return "false"

    return ','.join(intersection)


# keep this function call here
print(FindIntersection(input()))
