from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        
       jumps = 0
       left, right = 0, 0

       while right < len(nums)-1:
           farthest = 0
           for i in range(left,right + 1):
               farthest = max(farthest, i + nums[i])
           left = right+1
           right = farthest
           jumps += 1
     
       return jumps
                
    jump(self=0,nums=[2,3,1,1,4])
    