

n = 5
limit = 2
 
 
class Solution(object):
    def distributeCandies(self, n, limit):
    
        limit += 1
        count = 0

        for child1 in range(limit):
            for child2 in range(limit):
                for child3 in range(limit):

                    if child1 + child2 + child3 == n:
                        count += 1
        return count
    
    
s = Solution()
print(s.distributeCandies(n, limit))
