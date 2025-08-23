"""
input = height: int [] of length n
output = maxWater = int

calculate the max number of water that can a "container" can store. A container is considered the area under two indexes, with their height marked off by the value at the index.

Cases:
1)

Psuedo:
start = 0
end = final index of the height array
maxArea

while the start and end are not the same:
    height = min(height[start], height[end])
    area = height * (end - start)
    if area > maxArea:
        maxArea = area
    start += 1
    end -+ 1
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = -1

        while start < end:
            minHeight = min(height[start], height[end])
            # end - start would be the length of the container
            area = minHeight * (end - start)

            if area > maxArea:
                maxArea = area

            # use taller height
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return maxArea