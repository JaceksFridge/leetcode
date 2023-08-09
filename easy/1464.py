


nums = [3,7]


class Solution:
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return (nums[0]-1) * (nums[1]-1)
        
        
s = Solution()
print(s.maxProduct(nums))
