

s = "pwwkew"

class Solution(object):
    def lengthOfLongestSubstring(self, s):


        hashmap = {}
        max_count = 0
        start = 0
        
        for i, letter in enumerate(s):
            end = i
            
            if letter in hashmap and hashmap[letter] >= start:
                start = hashmap[letter] + 1
                
            hashmap[letter] = i
            max_count = max(max_count, end - start + 1)
        return max_count

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
