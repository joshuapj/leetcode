"""
input = nums: int []
output = ret: bool

see if there are 3 numbers in the given array which ascend in value given the order of the array.

Cases:
1) there is only one value in the array
2) there are 3 values which ascend in value
3) there are no values which ascend in value

Psuedo:
init i and j to big numbers

for k in nums:
    if k <= i:
        set i to the smallest
    elif k <= j:
        found a number larger than i, but smaller than k
    else:
        found three consiecutive numbers return true
return false

"""
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 2**32
        j = 2**32

        for k in nums:
            if k <= i:
                i = k
            elif k <= j:
                j = k
            else:
                return True
        return False
