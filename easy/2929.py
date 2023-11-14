

n = 5
limit = 2

class Solution(object):
    def distributeCandies(self, n, limit):



        result = 0

        for i in range(min(n, limit) + 1):

            second_min = max(0, n - i - limit)
            second_max = min(limit, n - 1)
            
            result += second_max - second_min + 1

            
        return result
    
    
s = Solution()
s.distributeCandies(n, limit)