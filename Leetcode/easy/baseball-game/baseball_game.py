class Solution:
    def calPoints(self, operations):
        scores = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                scores.pop(-1)
            elif operations[i] == 'D':
                scores.append(2*int(scores[-1]))
            elif operations[i] == '+':
                scores.append(int(scores[-2]) + int(scores[-1]))
            else:
                scores.append(int(operations[i]))
        return sum(scores)
