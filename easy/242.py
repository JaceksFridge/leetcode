
s = "anagram"
t = "nagaram"

class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        s_set = set()
        t_set = set()
        
        for i in range(len(s)):
            s_set.add(s[i])
            t_set.add(t[i])

        if sorted(s_set) == sorted(t_set):
            return True


sol = Solution()
print(sol.isAnagram(s, t))
