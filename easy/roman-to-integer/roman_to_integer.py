"""
name: roman to integer
type: easy
link: https://leetcode.com/problems/roman-to-integer/
note: this is the effective solutions
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for char in s:
            total += translations[char]
        
        return total


x = Solution()
print(x.romanToInt("III"))