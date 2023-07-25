'''
link:
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

'''

from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = Counter(nums[:k])
        size = len(window)
        n = len(nums)
        running = sum(nums[:k])
        max_total = running if size == k else 0

        for i in range(k, n):
            out, v = nums[i-k], nums[i]
            window[out] -= 1
            if window[out] == 0:
                window.pop(out)
                size -= 1
            
            if v in window:
                window[v] += 1
            else:
                window[v] = 1
                size += 1
            
            running = running + v - out
            #print(f"{i}: {nums[i]}; {running} | {window}")
            if size == k and running > max_total:
                max_total = running

        return max_total

x = Solution()
y = x.maximumSubarraySum([2, 1, 5, 1, 3, 2], 3)

print(y)
