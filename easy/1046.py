

import heapq
stones = [2,7,4,1,8,1]

class Solution(object):
    def lastStoneWeight(self, stones):
        
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            
            if stone2 > stone1:
                heapq.heappush(heap, stone1 - stone2)
                
        return abs(heap[0] if heap else 0)
        
s = Solution()
print(s.lastStoneWeight(stones))
