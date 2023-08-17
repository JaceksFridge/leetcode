

s = "aaabc"

class Solution(object):
    def minimizedStringLength(self, s):
        return len(set(s))
    
    
sol = Solution()
print(sol.minimizedStringLength(s))


