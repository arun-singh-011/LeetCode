from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
     maxProfit=0 # Profit
     for r in range(1,len(prices)):
        if prices[r]>prices[r-1]:
           profit=prices[r]-prices[r-1]
           maxProfit+=profit

             
     
     print(f"max profit is:{maxProfit}")
     return maxProfit
    maxProfit(self=0,prices=[7,1,5,3,6,4])