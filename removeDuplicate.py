from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
     # Start from the second element
        for r in range(1,len(nums)):
         if nums[r] != nums[r-1]:
          nums[left]=nums[r]
          left += 1
        
        print(nums)
        return left   

    removeDuplicates(self=0,nums=[1,1,1,2,2,3])