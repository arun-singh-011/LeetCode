from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
     nums.sort()
     l = 1
     r = len(nums) - 1
     i = 0
     res = []
    

     for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
           continue

        l, r = i + 1, len(nums) - 1

        while l < r:
          threeSum = a + nums[l] + nums[r]
          if threeSum > 0:
             r -= 1
          elif  threeSum < 0:
             l += 1
          else:
             res.append([a, nums[l], nums[r]])
             l += 1
             while nums[l] == nums[l -1] and l < r:
                l += 1
     return res
 

    #  while l < r:

    #          if nums[l] + nums[r] > nums[i]:
    #                 r -= 1
            
    #          elif nums[l] + nums[r] > nums[i]:
    #                 l += 1
                    
    #          elif nums[l] + nums[r] == nums[i]:
    #                 print(l,r)
    #                 return [l,r]
      
    #  print([])
    #  return []
            
    
    threeSum(self=0,nums=[-1,0,1,2,-1,-4])