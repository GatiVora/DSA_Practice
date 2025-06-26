def left_rotate(arr):

    first = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
rotated_arr = left_rotate(arr)
print("Array after left rotation:", rotated_arr)