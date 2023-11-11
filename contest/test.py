

n = 10

import math

class Solution(object):
    def stringCount(self, n):
    


        binomial = int(math.factorial(n) / (math.factorial(4) * math.factorial(n - 4)))
        
        permutations = int(math.factorial(4) / math.factorial(2))
        
        rest_positions = (n - 4)
        
        print(binomial, permutations, rest_positions)
        
        return binomial * permutations * 24**rest_positions
    
 
        
    
 
s = Solution()
print(s.stringCount(n))

            
# 778 467 755 520      
# 526 083 947 580