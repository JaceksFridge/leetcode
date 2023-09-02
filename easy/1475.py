

prices = [8,4,6,2,3]

class Solution(object):
    def finalPrices(self, prices):
        
        masterarr = []
        for i, price in enumerate(prices):
            print(i)
            if prices[i] < prices[i+1]:
                masterarr.append(price)
            elif not prices[i+1]:
                masterarr.append(price)
            else:
                masterarr.append(prices[i] - prices[i+1])
        return masterarr

                
sol = Solution()
print(sol.finalPrices(prices))
