

# class Solution(object):
#     def lengthOfLastWord(self, s):

#         words = s.strip().split(" ")
#         the_word = words[-1]
#         return len(the_word)


# sol = Solution()
# sol.lengthOfLastWord(s)
        
        
        


class Solution(object):
    def lengthOfLastWord(self, s):

        count = 0
        i = len(s) -1
        
        while (i >= 0 and s[i] == ' '):
            i -= 1
        while (i >=0 and s[i] !=  ' '):
            i -= 1
            count += 1
        return count


sol = Solution()
sol.lengthOfLastWord(s)