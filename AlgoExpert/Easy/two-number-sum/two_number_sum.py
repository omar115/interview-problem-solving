'''
Given an array of distinct integers and an integer representing the target sum, 
we are asked to implement a function that is going to find out whether 
there's a pair of numbers in the array that adds up to the target sum. 
If such pair exists, return the pair in any order; otherwise return an empty array. 
We cannot add a number to itself to get the target sum.
'''

'''
# bad approach: 
# time: O(n^2)
# space: 0(1)
 
def two_number_sum(nums, target):
    if len(nums) < 2:
        return nums
    for i in range(len(nums)):
        firstNum = nums[i]
        j = i + 1
        while j < len(nums):
            secondNum = nums[j]
            if firstNum + secondNum == target:
                return [i, j]
            j = j + 1
    
    return []

print(two_number_sum([1,2,5,7,4], 7))

'''