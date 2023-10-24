

nums = [1,2,3]

class Solution(object):
    def pivotIndex(self, nums):
        
        
        leftsum = 0
        for i, num in enumerate(nums):
            rightsum = 0
            for j in range(i+1, len(nums)):
                rightsum += nums[j]
            
            # print(leftsum, rightsum)
            if leftsum == rightsum:
                return i
            leftsum += num
        return 1
    
s = Solution()
print(s.pivotIndex(nums))
