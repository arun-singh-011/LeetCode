from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k % len(nums)
        
        l,r=0,len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l] ,nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        print(nums)
         
        # length=len(nums)
        # r=length-1
        # l=0
        # for l in range(0,length):
        #     print(f"left at:{nums[l]}")
        #     print(f"right at:{nums[r]}")
        #     print(nums)
            # nums.insert(0,nums.pop())
            # nums[r]=nums[r-k]
                    # r-=1
           # while l<(r-k):

    rotate(self=0,nums=[1,2,3,4,5,6,7],k=3)