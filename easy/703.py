

import heapq
k = 3
nums = [4, 5, 8, 2]

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:min(k, len(nums))]
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            heapq.heappushpop(self.heap, nums[i])
 
 
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    

obj = KthLargest(k, nums)

obj.add(3)
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)