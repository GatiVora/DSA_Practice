def find_sec_largest(arr):
    large  = second_large = float('-inf')
    for num in arr:
        if num> large:
            second_large = large
            large = num
        elif num > second_large and num != large:
            second_large = num
    return second_large 

arr = [1,3,5,9,8]
find_sec_largest(arr)

print("The second largest element in the array is:", find_sec_largest(arr))
