from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = 0
        for r in range(0,n):
            if nums[r]!=0:
                nums[l]=nums[r]
                nums[r]=0
             
                l += 1
                r+=1
                print(nums)
            elif nums[r]==0:
                r+=1
                l+=0

                print(nums)
        print(nums)
      
       
    moveZeroes(self=0,nums=[0,1,0,3,12])