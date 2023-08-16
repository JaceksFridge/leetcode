
s = "anagram"
t = "nagaram"

class Solution(object):
    def isAnagram(self, s, t):
        
        if sorted(s) == sorted(t):
            return True



sol = Solution()
print(sol.isAnagram(s, t))
