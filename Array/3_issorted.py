def isSorted(nums):
    for i in range(1,len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True

nums = [1, 2, 3, 8, 5]
if isSorted(nums):
    print("The array is sorted.")
else:
    print("The array is not sorted.")