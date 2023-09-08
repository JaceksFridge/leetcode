

words = ["cd","ac","dc","ca","zz"]

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        
        
        hashmap = { }
        
        for word in words:
            
            s_word = "".join(sorted(word))
            if s_word in hashmap:
                hashmap[s_word] += 1
            
            else:
                hashmap[s_word] = 0
                
        count = 0
        for value in hashmap.values():
            count += value
        return count


sol = Solution()
print(sol.maximumNumberOfStringPairs(words))
