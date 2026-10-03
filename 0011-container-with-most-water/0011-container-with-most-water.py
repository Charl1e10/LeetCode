class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0
        highestwater = 0
        water = 0
        for i in range(len(height) - 1):
            difference = right - left
            height1 = height[right]
            height2 = height[left]
            if height1 >= height2:
               water = height2 * difference
               left += 1
            else:
                water = height1 * difference
                right -= 1
            
            if water > highestwater:
                highestwater = water
            
        return highestwater
