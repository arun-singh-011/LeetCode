class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

     i = 0
     j = 0
  
     for j in range(len(t)):
        if i < len(s) and t[j] == s [i]:
            i += 1
            j += 1
        elif t[j] != s [i]:
           i += 0
           j += 1
     print(i)
     if i != len(s):
        print(False)
        return False
     elif i == len(s): 
        print(True)
        return True
    
    isSubsequence(self=0,s="abc", t="ahbgdc")