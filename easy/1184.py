

distance = [1,2,3,4]
start = 0
destination = 3

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):

        forward_distance = 0
        backward_distance = 0
        
        for i in range(start, destination):
            forward_distance += distance[i]
            
        print(distance)
        distance = distance[destination:]
        
        for num in distance:
            backward_distance += num
            
        min_distance = min(forward_distance, backward_distance)
        return min_distance
        
        
s = Solution()
print(s.distanceBetweenBusStops(distance, start, destination))
