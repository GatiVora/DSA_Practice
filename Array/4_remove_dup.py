def remove_duplicates(arr):
    i , j = 0, 1
    while j<len(arr):
        if arr[j]!=arr[i]:
            i += 1
            arr[i] = arr[j]
        j += 1
    return i+1

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:length])
