# def total(numbers):
#   sum = 0
#   for num in numbers:
#     sum += num
#   return sum
   
# nums = [12,3,49,23]
# print("Sum: ", total(nums))

# REMOVE ELEMENT
# nums=[2,3,2,3]
# val = 2
# for num in nums:
#     nums.remove(val)
#     print(nums)

from typing import List

def removeElement(self, nums: List[int], val: int) -> int:
    c = nums.count(val)
    for i in range(c):
            nums.remove(val)
            print(c)
        # if val==3:
            # nums.remove(val)
            # nums.append(val)
            print(nums)
 
    nums.pop()
    print(nums)
 
removeElement(self=0,nums=[2,3,45,3,5,3,45,2,2,354,2,3],val=3)
# def removeElement(self, nums: List[int], val: int) -> int:
#  for val in nums:
#   nums.remove(val)
   
#  print(nums)
        
     
 