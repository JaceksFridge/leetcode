

n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1



class Solution(object):
    def isHappy(self, n, seen=None):

        if seen is None:
            seen = set()
        
        if n in seen:
            return False
        
        seen.add(n)
        sum = 0
        
        for digit in str(n):
            sum += int(digit) ** 2
            
        if sum == 1:
            return True
        else:
            return self.isHappy(sum, seen)
        
    

s = Solution()
print(s.isHappy(n))
