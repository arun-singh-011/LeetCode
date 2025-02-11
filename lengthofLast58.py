class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
    #  res=s.split()[-1]
    #  print(res)
    #  count=len(res)
    #  print(count)
     i,length=len(s)-1, 0

     while s[i] ==" ":
        i -= 1
     while i>=0 and s[i] != " ":
        length += 1
        i -= 1
     print(length)
     return length

    lengthOfLastWord(self=0,s="Hello World")