def findLargestElement(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1, 2, 3, 4, 5]
largest = findLargestElement(arr)
print("The largest element in the array is:", largest)