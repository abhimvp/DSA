def rotateArrayByOne(self, nums):
        temp=nums[0]
        n = len(nums)
        for i in range(1,n):
            nums[i-1]=nums[i]
        nums[-1]=temp
        return nums


# Input: nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
# Explanation: Initially, nums = [1, 2, 3, 4, 5]
# Rotating once to left -> nums = [2, 3, 4, 5, 1]

