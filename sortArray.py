from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#  My solution
     for num in nums2: 
        nums1.append(num) 

     while len(nums1) != m+n:
            nums1.remove(0)
             
     nums1.sort()
     print(nums1)   

# More optimal solution
# last index of nums1
        # last = m + n - 1

        # # Merge in reverse order
        # while m > 0 and n > 0:
        #     if nums1[m - 1] > nums2[n - 1]:
        #         nums1[last] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n - 1]
        #         n -= 1
        #     last -= 1
        
        # # fill nums1 with leftover nums2 elements
        # while n > 0:
        #     nums1[last] = nums2[n - 1]
        #     n, last = n-1, last - 1

    merge(self=0,nums1=[-1,0,0,3,3,3,0,0,0], m=6, nums2=[1,2,2], n=3)     