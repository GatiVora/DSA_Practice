def find_missing_number(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) // 2
    sum_of_elements = sum(arr)
    return total - sum_of_elements

# Example usage
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)