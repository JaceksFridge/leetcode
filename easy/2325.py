
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"


class Solution(object):
    def decodeMessage(self, key, message):
        
        hashmap = {" " : " "}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        res = ""
        alpha_count = 0
        
        for char in key:
            if char in hashmap:
                pass
            else:
                hashmap[char] = alpha[alpha_count]
                alpha_count += 1
                

        for k in message:
            res += hashmap[k]
        return res
        
sol = Solution()
print(sol.decodeMessage(key, message))