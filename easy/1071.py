

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
        
        
#         if len(str2) > len(str1):
#             str1, str2 = str2, str1
        
#         if str2 not in str1:
#             return ""

#         elif len(str1) % len(str2) == 0:
            
#             times = int(len(str1) / len(str2))
#             if str1.count(str2) != times:
#                 return ""
#             else:
#                 return str2
        
#         while len(str1) > len(str2):
#             str1 = str1[4:]
            
            
#         if str1 in str2 :
#             return str1
        
        
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
            
s = Solution()
print(s.gcdOfStrings(str1, str2))


