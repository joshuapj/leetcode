"""
input =     nums: int []
output =    nums: int[]

we need to put all of the 0's on one side. to do this we will need to "bubble down" all of the 0's from the left to the right

Case:
1) there are all 0's
2) there are all non-0's
3) there are only two values in the array
4) there is only one value in the array

Psuedo:
init two pointers, left, currat the start of the array

while left and curr < len(nums):
    if curr == 0:
        curr ++ since we need curr to be pointing to a value to switch with a 0
        continue
    if left != 0:
        left ++ since we need this to be a 0 to switch with a non-zero
        continue
    if val at curr, left are !=0 and == 0 respectively and left < curr:
        switch the values
    else:
        curr ++ 
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, curr = 0, 0

        while curr < len(nums) and left < len(nums):
            if nums[curr] == 0:
                curr += 1
                continue
            if nums[left] != 0:
                left += 1
                continue
            if nums[curr] != 0 and nums[left] == 0 and left < curr:
                nums[curr], nums[left] = nums[left], nums[curr]
            else:
                curr += 1
            

        