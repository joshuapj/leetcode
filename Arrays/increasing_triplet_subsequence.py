"""
input = nums: int []
output = ret: bool

see if there are 3 numbers in the given array which ascend in value given the order of the array.

Cases:
1) there is only one value in the array
2) there are 3 values which ascend in value
3) there are no values which ascend in value

Psuedo:
init j and k to big numbers

for i in nums:
    if i <= j:
        set j to the smallest
    elif i <= k:
        found a number larger than j, but smaller than k
    else:
        found a three consiecutive numbers return true
return false

"""
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        j = 2**32
        k = 2**32
        
        for i in nums:
            if i <= j:
                j = i
            elif i <= k:
                k = i
            else:
                return True
        return False
