

s = "babgbag"
t = "bag"


class Solution(object):
    def numDistinct(self, s, t):
        
        hashmap = {} # number of solution : [indexes]
        hashmap_counter = 1
        
        for i in range(1):
            
            combi = []
            active_index = 0

            
            for index, letter in enumerate(s):
                if letter == t[active_index]:
                    combi.append(index)
                    
            hashmap[hashmap_counter] = combi

        
        print(hashmap)
        
        
        
sol = Solution()
sol.numDistinct(s, t)
        