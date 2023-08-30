

# word1  = ["abc", "d", "defg"]
# word2 = ["abcddefg"]

# class Solution(object):
#     def arrayStringsAreEqual(self, word1, word2):
        
#         master1 = ""
#         master2 = ""
        
#         for s in word1:
#             master1 += s
#         for s in word2:
#             master2 += s
            
#         return master1 == master2
        
# sol = Solution()
# print(sol.arrayStringsAreEqual(word1, word2))




class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):

         
        return "".join(word1) == "".join(word2)
        
sol = Solution()
print(sol.arrayStringsAreEqual(word1, word2))