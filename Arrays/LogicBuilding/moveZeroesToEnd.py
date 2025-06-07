# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in place, without making a copy of the array.
# Input: nums = [0, 1, 4, 0, 5, 2]
# Output: [1, 4, 5, 2, 0, 0]
# Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same
# Input: nums = [0, 0, 0, 1, 3, -2]
# Output: [1, 3, -2, 0, 0, 0]
# Explanation: All 3 zeroes are moved to the end and the order of the other elements stay the same
# Input: nums = [0, 20, 0, -20, 0, 20]
# Output:
# [20, -20, 20, 0, 0, 0]
def moveZeroes(self, nums):
    j = -1

    # length of nums
    n = len(nums)

    # place the pointer j:
    for i in range(n):
        if nums[i] == 0:
            j = i
            break

    # no non-zero elements:
    if j == -1:
        return

    """Move the pointers i and j and swap accordingly"""
    for i in range(j + 1, n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


"""
Start by taking two pointers, i and j & initialize j to -1. The pointer j will be used to track the position of the first zero in the array that we encounter.
Use a loop to move through the array and place the pointer j at the index of the first zero. If the array does not contain any zeros, exit early as no further steps are needed.
Set the pointer i to j + 1. This positions i right after the first zero found by j. From here, i will start moving through the rest of the array to find non-zero elements.
Now move non zero elements:
Continue looping through the array with i.
Whenever i encounters a non-zero element, swap the elements at positions i and j. This effectively moves the non-zero element to the position of the first zero.
After the swap, update j to point to the next zero in the array. This is done by incrementing j by 1.
Repeat the process until i has traversed the entire array. By the end of the loop, all non-zero elements will have been moved to the front of the array in their original order, and all zeros will be moved to the end.
"""
