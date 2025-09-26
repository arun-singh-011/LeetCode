class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This is the solution by Neetcode:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1 
        for char in t:
            countT[char] = countT.get(char,0) +1
        return countS == countT


        #   Inefficient solution it was my solution:
        # sortedS = ''.join(sorted(s))
        # sortedT = ''.join(sorted(t))
        # print(sortedS)
        # print(sortedT)

        # if sortedT == sortedS:
        #     return True
        # else:
        #     return False


    isAnagram(self=0,s="anagram", t="nagaram")