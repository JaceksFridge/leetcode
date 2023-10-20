

s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class Solution(object):
    def checkDistances(self, s, distance):

        hashmap = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i, letter in enumerate(s):
            if letter in hashmap:
                hashmap[letter].append(i)
            else:
                hashmap[letter] = [i]


        for i, char in enumerate(alpha):
            delta = 0
            if char in hashmap and len(hashmap[char]) == 2:
                delta = hashmap[char][1] - hashmap[char][0] -1
                if delta != distance[i]:
                    return False
        return True
    
sol = Solution()
print(sol.checkDistances(s, distance))
