def move_zeros_end(nums):
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j+1,len(nums)):
            if nums[i] !=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1

# Example usage
arr = [0, 1, 0, 3, 12, 0]
move_zeros_end(arr)
print("Array after moving zeros to the end:", arr)