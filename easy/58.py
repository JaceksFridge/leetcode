

class Solution(object):
    def lengthOfLastWord(self, s):

        words = s.strip().split(" ")
        the_word = words[-1]
        return len(the_word)


sol = Solution()
sol.lengthOfLastWord(s)
        