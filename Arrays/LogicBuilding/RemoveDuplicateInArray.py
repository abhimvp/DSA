class Solution:
    def removeDuplicates(self, nums):  # Edge case: if list is empty
        if not nums:
            return 0

        # Initialize pointer for unique elements
        i = 0

        # Iterate through the list
        for j in range(1, len(nums)):
            """If current element is different
            from the previous unique element"""
            if nums[i] != nums[j]:

                """Move to the next position in
                the list for the unique element"""
                i += 1

                """ Update the current position 
                with the unique element"""
                nums[i] = nums[j]

        # Return the number of unique elements
        return i + 1


"""
Approach 
Initialize 2 variables i as 0 and variable j as 1, where i will track the position of the last unique element found and j will iterate through the array to find new unique elements.
Iterate in array using j from second element to the end of the array.
If the element at position j is different from the element at position i, it means a new unique element is found. This is because the array is sorted in non-decreasing order, so any new element that is different from the previous one must be unique.
When a new unique element is found, increment i to move to the next position for storing unique elements. Copy the element at position j to the new position at i. This ensures that the first i + 1 elements of the array are all unique.
Continue comparing elements and updating the array until j has iterated through the entire array. Once the loop completes, the value of i + 1 represents the number of unique elements in the array.
"""
