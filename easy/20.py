
s = "()"


class Solution(object):
    def isValid(self, s):
        
        
        stack = []
        
        if not s:
            return False
        
        for string in s:
            if string in "([{":
                stack.append(string)
            else: 
                if not stack or \
                    ( string == ')' and stack[-1] != '(' ) or \
                    ( string == ']' and stack[-1] != '[' ) or \
                    ( string == '}' and stack[-1] != '{' ) :
                    return False
                stack.pop()
        return not stack

        

        
        
sol = Solution()
print(sol.isValid(s))

        