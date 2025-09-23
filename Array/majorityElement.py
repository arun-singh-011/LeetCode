from typing import List
from collections import Counter
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
    
     freq = {}
     for n in nums:
        freq[n] = 1 + freq.get(n,0)
   
     print(max(freq, key = freq.get))
    
    # Boyer-Moore algorithm
    
    
    
    
    
    
    
    
    
    
    
    majorityElement(self=0,nums=[2,2,2,6,2,3])
    
    
    
    
    
    
    
    
    
    
    #  res, count =0,0
    #  for n in nums:
    #     if count == 0:
    #         res = n
    #     count += (1 if n == res else -1)
    #  print(res)
    #  return res
    
########################################################
########################################################

    #  count = 1
    ##### HASHMAPS OR DICTIONARIES #####
    # city_map = {}
    # cities = ["Calgary", "Vancouver","Toronto"]
    # city_map["Canada"] = []
    # city_map["Canada"] += cities
    #  Use default dict
    # hashmap.keys()
    # hashmap.values()
    # hashmap.items()


    #  r=0
    #  while r < len(nums):
    #       count = 1
    #       while nums[r]==nums[r-1]:
    #          r += 1
    #          count += 1

    #  print(count)
    #  for r in range(1,len(nums)):
    #    if nums[r]==nums[r-1]:
    #      count += 1
    #      r += 1
    #      print(f"frequency is: {count}")  
    #  print(f"Majority number is: {nums[r]}")  
 
