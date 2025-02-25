from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:     
        l = 0
        r = len(numbers) - 1

        while l < r:
             if numbers[l] + numbers[r] > target:
                    r -= 1
            
             elif numbers[l] + numbers[r] < target:
                   l += 1
                   
             elif numbers[l] + numbers[r] == target:
                     print(l+1,r+1)
                     return [l+1,r+1]
        
   
    twoSum(self=0,numbers=[5,25,75], target=100)