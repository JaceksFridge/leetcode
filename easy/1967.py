
patterns = ["a","abc","bc","d"]
word = "abc"

class Solution:
    def numOfStrings(self, patterns, word):
        
        count = 0
        for pat in patterns:
            if pat in word:
                count += 1
        return count
    
s = Solution()
s.numOfStrings(word, patterns)




# create count = 0
# loop over array
    # compare i if included in word
        # if yes - count ++

# return count