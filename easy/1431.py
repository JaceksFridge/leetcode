

candies = [2,3,5,1,3]
extraCandies = 3

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        
        master = []
        
        highest = max(candies)


        for candy in candies:
            if candy + extraCandies >= highest:
                master.append(True)
            else:
                master.append(False)

        return master

sol = Solution()
print(sol.kidsWithCandies(candies, extraCandies))
