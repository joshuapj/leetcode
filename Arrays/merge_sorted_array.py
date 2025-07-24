import bisect
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1       # let i be the location of the last actual element in nums1
        j = n - 1       # let j be the last location in nums1
        k = m + n - 1   # let k be the last location in m, including 0's

        # order is reversed (right to left)
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1

            k = k - 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        