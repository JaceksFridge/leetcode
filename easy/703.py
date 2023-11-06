

k = 3
nums = [4, 5, 8, 2]

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
 
 
    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        print(self.nums)
        return self.nums[self.k - 1]
    
    def print_val(self):
        print(self.nums)
    

obj = KthLargest(k, nums)

obj.add(3)
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

obj.print_val()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)