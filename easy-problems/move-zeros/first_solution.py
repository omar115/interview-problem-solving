"""
leetcode link: https://leetcode.com/problems/move-zeroes/

solution type: mathematically logic

"""

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [ num for num in nums if num != 0 ] + [0] * (nums.count(0))
        print(nums)
        

x = Solution()
x.moveZeroes([0,1,0,3,12])