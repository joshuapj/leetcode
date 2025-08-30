"""
input   =   nums:   int []
output  =   answer: int []

For every item in the array, create a return array where the value stored at the index is equal to the product of every item in the array besides the current item.

Psuedo:
prefix [] = array containing the value of the prods  up until a given index.
postfix [] = array containing the value of the prods before a given index

prefix:
for i in range(len(nums)):
    if i is 0:
        let postfix[0] = nums[0]
    else:
        prefix[i] = prefex[i-1] * nums[i]

postfix. start at the end and go backwards. basically reverse of the prefix
for i in range(len(nums) - 1, 0, -1)
    if i == len(nums) - 1:
        let postfix[i] = nums[i]
    else:
        postfix[i] = postfix[i+1] * nums[i]

after we do that, just multiply the prefix by postifx for location i in nums
"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        
        # get the value of all the numbers before the index
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1]*nums[i]
        print(prefix)

        # populate in reverse, getting all values of a number after an index
        for i in range(len(nums) -1, 0, -1):
            if i == (len(nums) - 1):
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]
        
        print(postfix)

        # multiply postfix by prefix for a given index
        for i in range(len(nums)):
            if i == 0:
                nums[i] = 1 * postfix[i+1]
            elif i == len(nums) - 1:
                nums[i] = 1 * prefix[i-1]
            else:
                nums[i] = prefix[i-1] * postfix[i+1]
        return nums