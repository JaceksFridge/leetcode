

sentence = "thequickbrownfoxjumpsoverthelazydog"

class Solution(object):
    def checkIfPangram(self, sentence):

        sentence = set(sentence)
        if len(sentence) == 26:
            return True
        else:
            return False
        
        
sol = Solution()
print(sol.checkIfPangram(sentence))
