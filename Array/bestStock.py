from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 # Buy
        r=1 # Sell
        maxProfit=0 # Profit

#  Neetcode soln
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #      profit = prices[r]-prices[l]
        #      maxProfit=max(maxProfit,profit)
             

        #     else:
        #        l=r
        #     r += 1
        # print(maxProfit)
        # return maxProfit
     

    #  My Solution
        for r in range(0,len(prices)):
            if prices[l]>prices[r]:
       
               l=r

            elif prices[l]<prices[r]:
             profit=prices[r]-prices[l]
             maxProfit  = max(maxProfit,profit)
  
        print(maxProfit)
        return maxProfit
 
             
       
            
 
        print(maxProfit)
 
    
    maxProfit(self=0,prices=[7,1,2,6,3])