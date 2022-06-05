class Solution:
    def moveZeroes(self, li) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li2=[]
        li3=[]
        for i in range(len(li)):
            if li[i] != 0:
                li2.append(li[i])
            else:
                li3.append(li[i])
        for i in range(len(li3)):
            li2.append(li3[i])
        print('final result \n ', li2)
        return li2


li = [0, 1, 0, 3, 12]
a = Solution()
a.moveZeroes(li)