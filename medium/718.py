

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

class Solution(object):
    def findLength(self, nums1, nums2):
        
        max_length = 0
        
        start = 0
        end = 1

        
        while end <= len(nums1):
            
            idx = nums2.index(nums1[start])
            substr = nums2[idx:]
            
            count = 1
            while nums1[end] == substr[end]:
                count += 1
            
            max_length = max(max_length, count)
            start += 1
            end = start + 1
                
        return count
        
        
s = Solution()
s.findLength(nums1, nums2)