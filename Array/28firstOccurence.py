class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
     if needle==" ":
       return -1

     for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i + len(needle)] == needle:
           return i
     return -1

    strStr(self=0,haystack="sadbutbad",needle="bad")