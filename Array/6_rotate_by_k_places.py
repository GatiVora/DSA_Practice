def rotate_left(nums,k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
rotated_nums = rotate_left(nums, k)
print("Array after left rotation by", k, "places:", rotated_nums)
