'''
https://leetcode.com/problems/baseball-game/

'''

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for num in range(len(operations)):
            if operations[num] == 'C':
                li.pop()
            elif operations[num] == 'D':
                li.append(int(li[-1]) * 2)
            elif operations[num] == '+':
                li.append(int(li[len(li)-1]) + int(li[len(li)-2]))
            else:
                li.append(int(operations[num]))
        
        return sum(li)


x = Solution()
print(x.calPoints(["5","-2","4","C","D","9","+","+"]))
