

s="race a car"


class Solution(object):
    def isPalindrome(self, s):
        
        s = list(s.lower())
        
        pl = 0
        pr = len(s) - 1
        
        while pl < pr:
            
            if not s[pl].isalnum():
                pl += 1
                continue
            
            elif not s[pr].isalnum():
                pr -= 1
                continue
            
            elif s[pl] != s[pr]:
                return False

            pl += 1
            pr -= 1
        
        return True
        
sol = Solution()
print(sol.isPalindrome(s))
