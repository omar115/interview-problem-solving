class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li1 = []
        li2 = []
        for _ in range(len(nums)):
            if nums[_] == 0:
                li1.append(nums[_])
            else:
                li2.append(nums[_])
        final = li2 + li1
        return final


x = Solution()
print(x.moveZeroes([0,1,0,3,12]))