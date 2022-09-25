'''
Given an array of distinct integers and an integer representing the target sum, 
we are asked to implement a function that is going to find out whether 
there's a pair of numbers in the array that adds up to the target sum. 
If such pair exists, return the pair in any order; otherwise return an empty array. 
We cannot add a number to itself to get the target sum.
Note: it is similar to Leetcode two sum problem but little bit complex
'''


# approach -1: (nested loop)
# time: O(n^2), space: O(1)

# def two_number_sum(nums, targetSum):
#     for i in range(len(nums) - 1):
#         firstNum = nums[i]
#         for j in range(i + 1, len(nums)):
#             print(j)
#             secondNum = nums[j]
#             if firstNum + secondNum == targetSum:
#                 return [ firstNum, secondNum ]
    
#     return []

# print(two_number_sum([3,5,-4,8,11,1,-1,6], 10))

#----------------------------------------------------------------

# approach-2 (hash table) 
# time: O(n), space: 0(n)

# def two_number_sum(array, targetSum):
#     nums = {}
#     for num in array:
#         if targetSum - num in nums:
#             return [ targetSum - num, num ]
#         else:
#             nums[num] = True
#     return []

# print(two_number_sum([3,5,-4,8,11,1,-1,6], 10))


#----------------------------------------------------------------

# approach - 3 (sorted search)
# O(nlog(n)) time | O(1) space

def two_number_sum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [ array[left], array[right] ]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
