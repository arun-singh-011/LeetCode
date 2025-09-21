from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                r += 1
                l += 1
                
            else:
                r += 1
           
       
            print(l)
      

    removeDuplicates(self=0,nums=[1,1,1,2,2,2,3,3,4,4,4,4])