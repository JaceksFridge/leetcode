

words = ["Hello","Alaska","Dad","Peace"]


class Solution(object):
    def findWords(self, words):
        
        
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        
        masterarr = []
        
        for word in words:
            setw = set(word.lower())
            if setw.issubset(s1) or setw.issubset(s2):
                masterarr.append(word)
            elif setw.issubset(s3):
                masterarr.append(word)
                
        return masterarr
        
        
sol = Solution()
print(sol.findWords(words))
