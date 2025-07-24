from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVals = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in prevVals:
                return [prevVals[diff], i]
            prevVals[nums[i]] = i