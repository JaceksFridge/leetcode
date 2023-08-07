

s = "is2 sentence4 This1 a3"

class Solution:
    def sortSentence(self, s: str) -> str:
        
        returnArr = []
        opArr = s.split(' ')
        looper = 0

        while looper < 9:
            
            
            for i in opArr:
                if str(looper) in i:
                    i = i[:-1]
                    returnArr.append(i)
            
            looper += 1
            
        returnArr = ' '.join(returnArr)
        return returnArr

soy = Solution()
print(soy.sortSentence(s))
