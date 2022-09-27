'''
Given an array of integers that are sorted in increasing order,
we are asked to write a function that squares all the integers in the array 
and returns them in a new array. 
The returned array must be sorted in increasing order as well.

example:
input = [-3, -1, 2, 5, 10]
output = [100, 25, 9, 4, 1]
'''

# approach: for loop , O(nlog(n)) time | O(n) space
# def sorted_squared_array(array):
#     li = []
#     for i in array:
#         li.append(i*i)
    
#     li.sort(reverse=True)
#     return li

# print(sorted_squared_array([-3, -1, 2, 5, 10]))

# approach: two pointers, O(n) time | O(n) space

def sorted_squared_array(array):
    sortedSquare = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquare[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquare[idx] = largerValue * largerValue
            largerValueIdx -= 1
    
    return sortedSquare

print(sorted_squared_array([-4, 1, 2]))

