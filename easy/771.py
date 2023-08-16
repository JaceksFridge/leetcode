
jewels = "01"
stones = "01234001701"

class Solution(object):
    def numJewelsInStones(self, jewels, stones):


        counter = 0
        
        for x in stones:
            if x in jewels:
                counter += 1
        return counter








        # counter = 0
        # while jewels in stones:
            
        #     ids = stones.index(jewels)
        #     stones = stones[:ids] + stones[ids+len(jewels):]
        #     counter += 1
            
        # return counter


sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
