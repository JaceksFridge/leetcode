

nums = [5,3,6,1,12]
og = 3


class Solution(object):
    def findFinalValue(self, nums, og):
        
        while og in nums:
            og *= 2
        return og
        
        
        
        
        
        
        
        
        # hashmap = { val : index }

        # loop i, num  in nums 
            # hashmap[i] = num
        
        # while og in hashmap:

            # og = og * 2
            
        # return og
sol = Solution()
print(sol.findFinalValue(nums, og))
