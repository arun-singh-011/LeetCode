from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

# We have a better solution using hashset like here:


       hashset = set()

       for n in nums:
           if n in hashset:
               return True
           hashset.add(n)
       return False



    # This solution is done by Arun Singh on Sep 24, 2025 06:09 P.M. Vancouver Time
       l = 1
       nums.sort()
        

       for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
               print(True)
       return False
           
                
            








    containsDuplicate(self=0,nums=[0])
