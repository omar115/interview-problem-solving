"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # from leetcode, you will get TLE for this solution
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] == nums[j]:
        #             return True
        #         j += 1
        # return False

        # it will be accepted, took o(nlogn) time because
        # sorting has O(nlogn) time complexity
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False


x = Solution()
print(x.containsDuplicate([1, 2, 3]))
