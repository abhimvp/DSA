class Solution:
    def unionArray(self, nums1, nums2):
        union = []  # union set

        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            # case 1 and 2
            if nums1[i] <= nums2[j]:
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            # case 3
            else:
                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1

        # if any elements left in nums1
        while i < n:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        # if any elements left in nums2
        while j < m:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        return union
