
s = "xyzzaz"


class Solution(object):
    def countGoodSubstrings(self, s):
        

        start = 0
        end = 2
        count = 0
    
        while (end <= len(s)):
            
            substring = s[start:end+1]
            
            if len(set(substring)) == 3:
                count += 1
            
            start += 1
            end += 1
        
        
        return count
        

sol = Solution()
print(sol.countGoodSubstrings(s))
