

answerKey = "TTFTTFTT"
k = 1

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        
        max_length = 0
        
        count_t = 0
        count_f = 0

        left = 0
        right = 0
        
        while right < len(answerKey):
            
                
            if answerKey[right] == "T":
                count_t += 1
            else:
                count_f += 1
                    

            while min(count_t, count_f) > k:
                if answerKey[left] == "T":
                    count_t -= 1
                else:
                    count_f -= 1
                left += 1
                
            right += 1
            max_length = max(max_length, right - left)
                
        return max_length



s = Solution()
print(s.maxConsecutiveAnswers(answerKey, k))
