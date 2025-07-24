from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1 

        # in edge case where there are no items in list
        if len(nums) == 0:
            return;

        while i < j:
            if nums[i] == val:
                if nums[j] == val:
                    j = j - 1
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]

            i = i + 1

        while j < len(nums):
            if nums[j] == val:
                nums.pop(j)
            else:
                j = j + 1
