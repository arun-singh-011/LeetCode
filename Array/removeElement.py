from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         
     l = 0
     i = 0

     for l in range(0,(len(nums))):
        if nums[l] != val:
           nums[i] = nums[l]
           i += 1
     print(i)
     
 

    removeElement(nums=[0,1,2,2,3,0,4,2],val=2,self=0)