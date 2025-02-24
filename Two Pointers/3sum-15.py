from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
     l = 0
     r = len(nums) - 1
     x = 0
     res = []
     nums.sort()
     print(nums)
     while l < r:
        if nums[l] + nums[r] + x == 0:
           y = nums[l]
           z = nums[r]
           print(nums[l])
           print(nums[r])
           res.append(y)
           res.append(z)
           res.append(x)
           print(res)
           l += 1
           r -= 1
     
        else:
           l += 1 
           r -= 1
    

     return nums[l], nums[r]
    
    threeSum(self=0,nums=[-1,0,1,2,-1,-4])