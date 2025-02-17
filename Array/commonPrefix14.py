from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
   
     res=""
     for i in strs:
        for s in strs[0]:
           if s[i]!=strs[0][i]:
            return res
     res=strs[0][i]
      
     
      
    longestCommonPrefix(self=0,strs=["flower","flow","flight","flood"])  