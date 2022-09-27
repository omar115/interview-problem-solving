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

# approach: two pointers, 

def sorted_squared_array(array):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left]**2 > array[right]**2:
            array[left] = array[right]**2
            left += 1
        
        else:
            array[left] = array[left]**2
            left += 1
    return array

print(sorted_squared_array([-4, 1, 2]))

