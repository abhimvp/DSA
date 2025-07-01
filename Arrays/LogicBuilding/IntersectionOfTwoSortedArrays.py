class Solution:
    def intersectionArray(self, nums1, nums2):

        intersection = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return intersection
