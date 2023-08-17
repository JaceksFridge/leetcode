

nums1 = [1,2,3]
nums2 = [2,4,6]



class Solution(object):
    def findDifference(self, nums1, nums2):
        masterlist = []
        
        set1, set2 = set(nums1), set(nums2)
        
        masterlist.append([list(set1.difference(set2))])
        masterlist.append([list(set2.difference(set1))])
        
        return masterlist
        
sol = Solution()
print(sol.findDifference(nums1, nums2))



# [set(a)-set(b), set(b)-set(a)]
