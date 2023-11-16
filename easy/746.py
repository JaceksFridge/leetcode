

cost = [0,1,2,2]

class Solution(object):
    def minCostClimbingStairs(self, cost):


        spot = 0
        if len(cost) == 3:
            spot = 1
        elif cost[1] <= cost[0]:
            spot = 1
        else:
            spot = 0
            
        counter = cost[spot]


        while spot + 2 < len(cost):
            
            if spot+2 == len(cost) - 2:
                if cost[spot+2] < (cost[spot+1] + cost[-1]):
                    counter += cost[spot+2]
                    return counter
            
            single = cost[spot+1]
            double = cost[spot+2]
        
            if double <= single:
                spot += 2
            else:
                spot += 1
            
            counter += cost[spot]
            
        return counter
    
s = Solution()
print(s.minCostClimbingStairs(cost))
