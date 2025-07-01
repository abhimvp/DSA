class Solution:
    # Function to find the leaders in an array.
    def leaders(self, nums):
        ans = []

        if not nums:
            return ans

        # Last element of the list is always a leader
        max_val = nums[-1]
        ans.append(nums[-1])

        # Check elements from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_val:
                ans.append(nums[i])
                max_val = nums[i]

        """Reverse the list to match
        the required output order"""
        ans.reverse()

        # Return the leaders
        return ans
