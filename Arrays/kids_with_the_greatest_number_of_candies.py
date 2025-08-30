'''
input = candies: int []
        extraCandies: int

output = res: bool []

they want us to find if the current child's candy + extraCandy is greater or equal to the max candy that all the kids have

Edge Cases:
- Happy Path: candies = [2,3,5,1,3], extraCandies = 3
- Edge: candies = [1,1,1,1,1], extraCandies = 1

Psuedo:
maxCandy = max candy from candies
res = []
i = 0

res = [True, True]
.append = tagging on to the end

for i in range(length of candies)
    # we want to store the current childs candy + the extra
    newAmount = candies[i] + extraCandies
    if newAmount >= maxCandy:
        res.append(True)
    else:
        res.append(False)
return res

'''
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # get max candies
        maxVal = max(candies)
        res = []
        for i in range(len(candies)):
            # calculate
            newAmount = candies[i] + extraCandies
            if newAmount >= maxVal:
                res.append(True)
            else:
                res.append(False)
        return res