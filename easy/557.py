

s = "Let's take LeetCode contest"
 
class Solution(object):
    def reverseWords(self, s):

        master_list = []
        words = s.split(" ")
        

        for word in words:
            master_list.append(word[::-1])
        return " ".join(master_list)
    
sol = Solution()
print(sol.reverseWords(s))
