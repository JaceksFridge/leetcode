

nums = [4,1,2,1,2]

class Solution(object):
    def singleNumber(self, nums):
        
        result = 0
        
        for num in nums:
            result = result ^ num

        return result
            
        
s = Solution()
s.singleNumber(nums)
        