

nums = [1,2,3]

class Solution(object):
    def pivotIndex(self, nums):
        
        
        leftsum = 0
        rightsum = sum(nums)
        for i, num in enumerate(nums):
            rightsum -= num

            if leftsum == rightsum:
                return i
            leftsum += num
        return -1
    
s = Solution()
print(s.pivotIndex(nums))
