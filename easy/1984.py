

nums = [9,4,1,7]
k = 2

class Solution(object):
    def minimumDifference(self, nums, k):

        nums.sort()
        min_delta = float('inf')
        left, right = 0, k-1
        while right < len(nums):
            
            min_delta = min(min_delta, nums[right] - nums[left])
            left += 1
            right += 1
        return min_delta

s = Solution()
s.minimumDifference(nums, k)
        