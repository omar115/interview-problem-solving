'''
https://leetcode.com/problems/concatenation-of-array/

'''

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return 2*nums


x = Solution()
print(x.getConcatenation(nums=[1, 2, 3]))