class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if nums[i] + nums[i + 1] == target:
                return nums[i], nums[i+1]



nums = [2, 7, 8, 9]
nums = [3, 2, 4]
target = 6
solve = Solution()
print(solve.twoSum(nums, target))