"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
 original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        easy solution: O(nlogn)
        using sorted() method we can directly check
        but time complexity is high and might not suitable for everywhere
        """
        # return sorted(s) == sorted(t)

        """
        ideal solution:
        using hash table, we can put the logic and 
        solve this problem. checking the number of
        occurances of each character is the solution
        
        complexity: O(n)
        
        """

        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1
        for value in count.values():
            if value != 0:
                return False

        return True


x = Solution()
print(x.isAnagram("silent", "listen"))
