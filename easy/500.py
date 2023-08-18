

words = ["Hello","Alaska","Dad","Peace"]


class Solution(object):
    def findWords(self, words):
        
        hashmap = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm")
        }
        
        
        masterarr = []
        
        for word in words:
            setw = set(word.lower())
            if setw.issubset(hashmap[1]):
                masterarr.append(word)
            elif setw.issubset(hashmap[2]):
                masterarr.append(word)
            elif setw.issubset(hashmap[3]):
                masterarr.append(word)
        return masterarr
        
        
sol = Solution()
print(sol.findWords(words))
