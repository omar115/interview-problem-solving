from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        right = len(nums) - 1
        left = 0
        li = []

        for i in range(len(nums)):
            if nums[left] + nums[right] == target:
                continue
            if nums[left] + nums[right] < target:
                li.append(nums[left] + nums[right])
                left += 1

            else:
                right -= 1

        return max(li)

x = Solution()
print(x.twoSum([34,23,1,24,75,33,54,8], 60))