"""There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
each sock, determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs
is .


"""


def solution(n, ar):
    count = 0
    for i in range(len(ar)):
        if ar.count(ar[i]) % 2:
            count += ar.count(ar[i]) / 2

x = solution(7, [1, 2, 1, 2, 1, 3, 2])

print(x)
