

str1 = "ABCABC"
str2 = "ABC"

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        
        if str2 not in str1:
            return ""

        elif len(str1) % len(str2) == 0:
            
            times = int(len(str1) / len(str2))
            if str1.count(str2) != times:
                return ""
            else:
                return str2
        
        while len(str1) > len(str2):
            str1 = str1[4:]
            
            
        if str1 in str2 :
            return str1
        
        
            
s = Solution()
print(s.gcdOfStrings(str1, str2))


