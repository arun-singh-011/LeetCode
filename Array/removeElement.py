from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         
        l = 0
       
        while l < len(nums):
            if nums[l] == val:
                nums.remove(nums[l])
                l += 1
                print("length of array", len(nums))
                 
                print(nums)
            elif nums[l] != val:
                l += 1
              
        return print(len(nums))

    removeElement(nums=[0,1,2,2,3,0,4,2],val=2,self=0)