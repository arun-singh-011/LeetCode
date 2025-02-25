from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap={} # VALUE: INDEX

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        
    twoSum(self=0,nums=[-1,-2,-3,-4,-5], target=-8)