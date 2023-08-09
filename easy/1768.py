

word1 = "abcd"
word2 = "pq"


class Solution:
    def mergeAlternately(self, word1, word2):

        merger = []
        length = max(len(word1), len(word2))
        while length > 0:
            
            if word1 != '':
                merger.append(word1[0])
                word1 = word1[1:]
                
            if word2 != '': 
                merger.append(word2[0])
                word2 = word2[1:]
            
            length -= 1
        return " ".join(merger)
    
    
s = Solution()
print(s.mergeAlternately(word1, word2))
