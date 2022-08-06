"""
leetcode: Palindrome Number
link: https://leetcode.com/problems/palindrome-number/

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        oldNumber = x
        newNumber = 0
        while x > 0:
            newNumber = newNumber * 10 + oldNumber % 10
            x = x // 10
        return newNumber == oldNumber
        

x = Solution()
print(x.isPalindrome(11))