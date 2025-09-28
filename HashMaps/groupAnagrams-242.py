from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
      groups = defaultdict(list)
      for char in strs:
         key = "".join(sorted(char))
         groups[key].append(char)
         
      return list(groups.values())







    groupAnagrams(self=0,strs=["eat","tea","tan","ate","nat","bat"])