from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
    #    Greedy Approach with moving the goal

       goal = len(nums) - 1
       for i in range(len(nums)-1,-1,-1):
           if i + nums[i] >= goal:
               goal = i
         
       if goal == 0:
           print(True)
       else:
           print(False)
                
    canJump(self=0,nums=[2,0,0])
    