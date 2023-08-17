

s = "abcabcbb"

class Solution(object):
    def lengthOfLongestSubstring(self, s):



        # hashmap 
        
        # sorted














        # hashmap = {}
        # alpha = "abcdefghijklmnopqrstuvwxyz"
        # for i in range(len(alpha)):
        #     hashmap[alpha[i]] = i + 1
        
        
        # master_count = 0
        # mini_count = 0    

        # for i in range(len(s)):
        #     if i == 0:
        #         mini_count += 1
        #         pass
        #     elif hashmap[s[i]] - 1 == hashmap[s[i-1]]:
        #         mini_count += 1
        #     else:
        #         if mini_count > master_count:
        #             master_count = mini_count
        #         mini_count = 0
        # return master_count
                
sol = Solution()
print(sol.lengthOfLongestSubstring(s))

