

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

class Solution(object):
    def mostWordsFound(self, sentences):


        longest = 0
        
        for sen in sentences:
            words = len(sen.split(" "))
            
            if words > longest:
                longest = words

        return longest
        
        
sol = Solution()
print(sol.mostWordsFound(sentences))
