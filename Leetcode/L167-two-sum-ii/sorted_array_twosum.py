from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        right = len(nums) - 1
        left = 0

        for i in range(len(nums)):
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1