


        # me

        # reverse sort list
            # loop till list empty
                # create mini
                # add index 1
                # pop index [0, 1] [len(-1)] 

        # return me

piles = [9,8,7,6,5,1,2,3,4]


class Solution:
    def maxCoins(self, piles):
        
        me = 0
        piles.sort(reverse=True)
        
        while len(piles) > 0:
            me += piles[1]
            del piles[0]
            del piles[1]
            del piles[-1]

        return me
            
s = Solution()
print(s.maxCoins(piles))
