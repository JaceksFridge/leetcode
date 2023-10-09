

distance = [1,2,3,4]
start = 0
destination = 3

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        
        forward_distance = 0
        backward_ditance = 0
        
        if start > destination:
            start, destination = destination, start
            
        forward = distance[start:destination]

        backward = distance[:start] + distance[destination:]
        
        for stop in forward:
            forward_distance += stop
        for stop in backward:
            backward_ditance += stop

        return min(forward_distance, backward_ditance)

        
s = Solution()
print(s.distanceBetweenBusStops(distance, start, destination))
