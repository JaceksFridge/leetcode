

nums = [3,2,4]
target = 6

class Solution(object):
    def twoSum(self, nums, target):
    
        
        # for i, n in enumerate(nums):
        #     rest = target - n
        #     if rest in nums[i+1:]:
        #         return [i, nums[i+1:].index(rest) + i + 1 ]
        
        
        
        prevMap = {} # val: index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
        
sol = Solution()
print(sol.twoSum(nums, target))
