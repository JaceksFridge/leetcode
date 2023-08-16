

# nums = [1,1,1,3,3,4,3,2,4,2]

# class Solution(object):
#     def containsDuplicate(self, nums):
        
#         nums = sorted(nums)
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
            
#         return False
# s = Solution()
# print(s.containsDuplicate(nums))








nums = [1,1,1,3,3,4,3,2,4,2]

class Solution(object):
    def containsDuplicate(self, nums):
        
        my_set = set()
        for x in nums:
            if x in my_set:
                return True
            my_set.add(x)
        return False
    

s = Solution()
print(s.containsDuplicate(nums))


        
        