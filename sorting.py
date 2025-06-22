def selection_sort(nums):
    for i in range(len(nums)):
        mini_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mini_idx]:
                mini_idx = j
        nums[i], nums[mini_idx] = nums[mini_idx], nums[i]
    return nums

def bubble_sort(nums):
    for i in range(len(nums)):
        did_swap = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                did_swap = True
        if not did_swap:
            break # no swaps means the list is sorted 
    return nums

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            # Swap if the current element is smaller than the one before it
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [4, 2, 7, 1]
sorted_nums = merge_sort(nums)
print(sorted_nums)

