class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sum_n = 0
        for i in range(1, n + 1):
            sum_n += i
        # Summation of first N natural numbers
        # sum1 = (N * (N + 1)) // 2
        sum_arr = 0
        for i in range(n):
            sum_arr += nums[i]
        return sum_n - sum_arr
