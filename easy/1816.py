

s = "Hello how are you Contestant"
k = 4



class Solution(object):
    def truncateSentence(self, s, k):

        words = s.split(" ")
        words = " ".join(words[:k])
        return words
        

sol = Solution()
sol.truncateSentence(s, k)
        