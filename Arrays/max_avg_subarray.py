"""
input:  nums = int []
        k   = int

output: nums = int []

find a continuos array of length k whose average is the greatest in the array

Cases:
    1) k is the length of the array
    2) k is less than the length of the array

Pseudo:
get the sum of the initial window
set the sum of the intial window as the max window
for i in range starting at k to length of nums:
    remove the value at the left
    add value to the right
    recalculate the sum
    check if its greater than the current max sum
return maxsum/k
"""
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         start = 0
#         end = k
#         maxAvg = -999
#         while end <= len(nums):
#             avg = sum(nums[start:end]) / k
#             if avg >= maxAvg:
#                 maxAvg = avg
#             end += 1
#             start += 1
#         return maxAvg
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # intialize the window
        window = sum(nums[0:k])
        maxWindowSum = window

        for i in range(k, len(nums)):
            # remove the element on the left
            window -= nums[i - k]
            # add element on the right
            window += nums[i]
            # see if the sum is greater than the max
            maxWindowSum = max(window, maxWindowSum)
        return maxWindowSum / k