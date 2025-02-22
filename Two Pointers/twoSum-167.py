from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

        # for l in range(0,len(numbers)):
        #     if r < len(numbers) and numbers[l] + numbers[r] == target:
        #         print(f"{[l,r]}")
        #         return [l+1, r+1]
              
        #     elif r < len(numbers) and numbers[l] + numbers[r] != target:
        #         r += 1 
        #         print(False)
        #         return False
                
        l = 0
        r = len(numbers) - 1

        while r < len(numbers) and l < len(numbers):
             if numbers[l] + numbers[r] > target:
                    r -= 1
                    # l += 1
             elif numbers[l] + numbers[r] < target:
                   l += 1
             elif numbers[l] + numbers[r] == target:
                     print(l+1,r+1)
                     return [l+1,r+1]
        
    # twoSum(self=0,numbers=[2,3,4], target=6)
    twoSum(self=0,numbers=[5,25,75], target=100)