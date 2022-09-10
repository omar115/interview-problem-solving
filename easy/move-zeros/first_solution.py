class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li1 = []
        li2 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                li1.append(i)
            else:
                li2.append(i)
            final = li2 + li1
            return final


x = Solution()
print(x.moveZeroes([0,1,0,2,12]))