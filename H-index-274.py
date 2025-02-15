from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
       
        # citations.sort()
        # h=0
        # paper=0
        # for i in range(len(citations)):
        #     if citations[i]>=h:
        #         # print(f"values: {citations[i]}")
        #         paper+=1
        #         h+=1
        #         print(f"values: {citations[i]} when h is {h} and paper is {paper}")
        #     else:
        #         paper+=0
        # print(paper)
        n = len(citations)
        paper_count = [0] * (n+1)

        for c in citations:
            paper_count[min(n,c)] += 1
        h = n
        papers= paper_count[n]

        while papers < h:
            h -= 1
            papers += paper_count[h]
        return h


             
                 

        
        
        
        
    hIndex(self=0,citations=[3,0,5,1,5])