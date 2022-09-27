'''
We are asked to write a function 
that is going to determine whether or not a given string is a palindrome, 
in other words, whether the given string reads the same backward as forward. 
If a string has zero or one character, it is a palindrome. 
The input string contains at least one character.

'''



'''
approach-1:  string reverse/slice | O(n^2) time | O(n) space

Note: str slices, in general, copy. 
That means that your function that does a slice for each of your string's n suffixes is doing O(n2) work.
Therefore, we should not use str.reverse or str.slice here.

'''

# def palindrome_check(word):
#     return word == word[::-1]

# print(palindrome_check('madam'))


# approach-2: two pointer | O(n) time | O(1) space
def palindrome_check(word):
    right = len(word) - 1
    for value in range (len(word)):
        if right == value:
            return True
        if word[value] == word[right]:
            right -= 1
        else:
            return False

print(palindrome_check('madam'))