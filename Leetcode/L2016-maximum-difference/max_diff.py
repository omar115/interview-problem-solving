from typing import List

# two pointer approach
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        l = 0
        ans = 0

        for r in range(1, len(nums)):
            if nums[r] < nums[l]:
                l = r
                continue
            else:
                ans = max(ans, nums[r] - nums[l])

        return ans if ans != 0 else -1


x = Solution()
print(x.maximumDifference([7,1,5,4]))