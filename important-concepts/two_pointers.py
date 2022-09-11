"""
tutorial link:
https://medium.com/@timpark0807/leetcode-is-easy-two-pointers-90b9b0f2eb43

strategy:
- if your input is a string or array, consider two pointer on your solution list
- stronger signals are:
* If we want to reduce nested loops to a single pass.
* If the input is sequenced or sorted.
* If we need to compare a value at one index with value at another index.
* If we need to make swaps between indices.
* If we partition the array.
"""

def check_palindrome_for_string_value(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


def check_palindrome_for_list(list):
    left = 0
    right = len(list) - 1
    while left < right:
        if list[left] != list[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

print(check_palindrome_for_string_value('madam'))
print(check_palindrome_for_list([1, 1, 1]))