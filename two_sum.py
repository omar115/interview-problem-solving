
def two_sum(nums, target):
    i = 0
    j = 0
    while i < len(nums) - 1:
        while j < len(nums):
            j = i + 1
            if nums[i] + nums[j] == target:
                return [i, j]
            j = j + 1
        i = i + 1


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))