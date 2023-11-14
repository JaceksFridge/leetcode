
s = "{"

import re

class Solution(object):
    def isValid(self, s):
        
        pattern = r"(\(\)|\{\}|\[\])+"
        match = re.fullmatch(pattern, s)
        
        return True if match else False
        
        
        


sol = Solution()
print(sol.isValid(s))

        