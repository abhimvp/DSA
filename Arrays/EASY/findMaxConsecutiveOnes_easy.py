class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count_ones = 0
        max_ones = 0
        print("Initializing count_ones and max_ones to 0")
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ones += 1
                print("count_ones:", count_ones)
            else:
                print("encountered a 0 at index", i)
                if count_ones > max_ones:
                    max_ones = count_ones
                    print("(c_ones > m_ones ) - max_ones:", max_ones)
                    count_ones = 0
                    print("count_ones:", count_ones)
                else:
                    print("max_ones:", max_ones)
                    print("count_ones:", count_ones)
                    count_ones = 0

        print("Final check after loop")
        if count_ones > max_ones:
            max_ones = count_ones
            print("Final max_ones:", max_ones)
        else:
            print("Final max_ones remains:", max_ones)

        return max_ones


# Main function
if __name__ == "__main__":

    nums = [
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]

    # Create an instance of the Solution class
    sol = Solution()
    ans = sol.findMaxConsecutiveOnes
    print(ans(nums))
