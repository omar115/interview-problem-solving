def find_palindrome_pattern(value):
    left = 0
    right = len(value) - 1

    for i in range(len(value)):
        if value[left] != value[right]:
            return False
        else:
            left += 1
            right -= 1
    
    return True


value = "ewe"
print(find_palindrome_pattern(value))
