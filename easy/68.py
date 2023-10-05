

a = "11"
b = "1"

class Solution(object):
    def addBinary(self, a, b):
        
        a = int(a, 2)
        b = int(b, 2)
        
        sum = a + b
        return bin(sum)[2:]
        

s = Solution()
s.addBinary(a, b)