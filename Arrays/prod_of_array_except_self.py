"""
input   =   nums:   int []
output  =   answer: int []

For every item in the array, create a return array where the value stored at the index is equal to the product of every item in the array besides the current item.

Pseudo:
APPROACH 1:
given [1,2,3,4]
we know that the produced array = [24, 12, 8, 6]
look for correlation between given array and product array:
maybe start thinking of the arrays in a circular fashion
[1,     2,      3,      4]
[24,    12,     8,      6]
[2*3*4, 1*3*4,  1*2*4,  1*2*3]  // using values
[1*2*3, 0*2*3,  0*1*3   0*1*2]  // using indexes

we can say, based on the above that at location, i and i+1, there is a common product being used:

copy = copy of nums
flipped_copy = flip of copy

for i in range(nums):
    flipped_copy *= nums
    nums = nums[1:] + nums[:1]
print(flipped_copy)

APPROACH 2:
given [1,2,3,4]
we know that the produced array = [24, 12, 8, 6]

keep a prefix array (product of all values before the an index)
prefix = []

for i in range(len(nums)):
    if i = 0:
        prefix.append(1)
    else:
        prefix.append(prefix[i-1] * nums[i])


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
        for i in range(len(nums) -1, -1, -1):
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