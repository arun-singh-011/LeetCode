import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

     l=0
     r=len(s)-1 
     
     while l < r :
        while l<r and not self.alphaNum(s[l]):
           l += 1
        
        while r > l and not self.alphaNum(s[r]):
           r -= 1

        if s[l].lower() != s[r].lower():
           return False
         
        l += 1
        r -= 1

     return True
    
    def alphaNum(self,c):
      return  (ord('A') <= ord(c) <= ord('Z') 
               or 
               ord('a') <= ord(c) <= ord('z') 
               or 
               ord('0') <= ord(c) <= ord('9'))


    # My solution
    #  s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    #  l=0
    #  r=len(s)-1 
     
    #  while l < r :
    #     if s[l] != s[r]:
    #        return False
         
    #     l += 1
    #     r -= 1

    #  return True

    isPalindrome(self=0,s="A  man, a plan, a canal: Panama")