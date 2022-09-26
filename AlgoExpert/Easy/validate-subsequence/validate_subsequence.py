'''
We are given two arrays of integers array and sequence. 
We are asked to implement a function that is going to check 
whether all the numbers in the sequence appear in the array 
and they appear in the same order. 
In other words, the function needs to find out 
if we can get the sequence array from the array, 
when we delete some or no elements in the array without 
changing the order of the remaining elements.

example:
array: [3, 1, 7, 5, 10, 2];
sequence: [1, 5, 2];
Output: true

'''

# two pointers | O(n) time | O(1) space
# def validateSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < array.length() and seqIdx < sequence.length():
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)


# two pointers | O(n) time | O(1) space
def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sequence)

print(validateSubsequence[1, 2, 3, 4, 5, 6], [1, 3, 5])