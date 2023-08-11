from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        li = []
        for i in range(len(nums)):
            if nums[i] in li:
                return True
            else:
                li.append(nums[i])
        
        return False


x = Solution()
y = x.containsDuplicate([1,2,3,4])
print(y)