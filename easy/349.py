

nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution(object):
    def intersection(self, nums1, nums2):


        return list(set(nums1) & set(nums2))
    
    
sol = Solution()
print(sol.intersection(nums1, nums2))
