class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[s[i]] = 1 + countT.get(s[i], 0)
        for c in countS:
            countS[c] != countT[c]
            return False

      

        #   Inefficient solution
        # sortedS = ''.join(sorted(s))
        # sortedT = ''.join(sorted(t))
        # print(sortedS)
        # print(sortedT)

        # if sortedT == sortedS:
        #     return True
        # else:
        #     return False


    isAnagram(self=0,s="anagram", t="nagaram")