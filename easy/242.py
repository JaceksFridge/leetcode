
s = "anagram"
t = "nagaram"

class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for c in s_count:
            if s_count[c] != t_count.get(c, 0):
                return False

        return True

sol = Solution()
print(sol.isAnagram(s, t))
