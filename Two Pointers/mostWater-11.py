from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

      l = 0
      r = len(height) - 1
      maxArea = 0
      while l < r:
         area = (r-l) * min(height[r],height[l])
         maxArea = max(maxArea,area)

         if height[l] <= height[r]:
            l += 1
            
         elif height[l] > height[r]:
            r -= 1
         
      print(maxArea)
      
    maxArea(self=0,height=[1,8,6,2,5,4,8,3,7])
