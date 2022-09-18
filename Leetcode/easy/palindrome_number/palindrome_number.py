"""
leetcode: Palindrome Number
link: https://leetcode.com/problems/palindrome-number/


Most possible solution types:
- string slicing
- mathematically expressions
- two pointers

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert = str(x)
        print(convert[::-1])
        if convert == convert[::-1]:
            return True
        else:
            return False

x = Solution()
print(x.isPalindrome(11))