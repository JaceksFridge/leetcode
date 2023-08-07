
n = 9

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        super_sum = 0
        
        for i in range(1, n+1):
   
            if i % 3 == 0:
                super_sum += i
            elif i % 5 == 0: 
                super_sum += i
            elif i % 7 == 0: 
                super_sum += i
            
        return super_sum

yoyoma = Solution()
print(yoyoma.sumOfMultiples(n))

    
    