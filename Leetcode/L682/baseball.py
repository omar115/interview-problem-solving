'''
https://leetcode.com/problems/baseball-game/

'''

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for num in range(len(operations)):
            if operations[num].isdigit():
                li.append(int(operations[num]))
            elif operations[num] == 'C':
                li.pop()
            elif operations[num] == 'D':
                li.append(li[-1] * 2)
            elif operations[num] == '+':
                li.append(li[len(li)-1] + li[len(li)-2])
        
        return sum(li)


x = Solution()
print(x.calPoints(['5', '2', 'C', 'D', '+']))
