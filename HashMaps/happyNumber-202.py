class Solution:
    def isHappy(self, n: int) -> bool:
     visit = set()
     while n not in visit:
        visit.add(n)
        n = self.sumOfSquares(n)

        if n == 1:
          return True
     return False
    def sumOfSquares(self, n: int) -> int:
    #  ToDo:
     output = 0
     while n: 
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 1
     return output
   #  h
   

    isHappy(self = 0, n = 19)