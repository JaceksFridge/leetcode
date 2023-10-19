
n = 6

class Solution(object):
    def tribonacci(self, n):

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 1:
            return 2
        else:
            arr = [0, 1, 1]
            
            for i in range(len(arr), n):
                
                next = arr[-1] + arr[-2] + arr[-3]
                arr.append(next)
                
            
            return arr[-3] + arr[-2] + arr[-1]
    
    
s = Solution()    
s.tribonacci(n)

