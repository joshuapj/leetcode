"""
input = flowerbed : int []
        n : int

output = ret: bool

check if there are enough strings of 3 0's such that all of the flowers given by n can be planted without having any 1's next to each other

Case:
1) the length of the flowerbed is 1
2) the flowerbed starts with consecutive 0's
3) the flowerbed ends with consecutive 0's
4) the flowerbed has all 0's :)

Psedo:
  check to make sure the flowerbed has a length greater than 1
  if it does not: 
      append 0 to start and end (prevent index oor)
  else if index 0, 1 are not planted:
      plant something at index 0
      decrement n
  
  for i in range (1, len(flowerbed) - 1):
      if flowebed[i-1], flowerbed[i] and flowerbed[i+1] are all 0:
          flowerbed[i] = 0
          decrement n
  
  if the last two indexes are consecutive 0's:
      n -= 1
"""
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #check that the length is more than 1
        if len(flowerbed) <= 1:
            # just add to the two ends so loop can still check n
            flowerbed = [0] + flowerbed + [0]
        # look at the start first
        elif flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        # start at 1 since we potentially appended to the array
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        # look at the end separately
        if flowerbed[len(flowerbed) -1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[0] = 1
            n -= 1
        return n <= 0