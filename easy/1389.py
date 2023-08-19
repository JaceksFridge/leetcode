


nums = [0,1,2,3,4]
index = [0,1,2,2,1]

class Solution(object):
    def createTargetArray(self, nums, index):
        
        target = []
        
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
            
        return target

        
sol = Solution()
print(sol.createTargetArray(nums, index))
