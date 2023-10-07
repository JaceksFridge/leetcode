

nums1 = [2,4]
nums2 = [1,2,3,4]


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        tresor = []
        
        for num in nums1:
            
            search = False
            found = False
            
            for number in nums2:
                
                if num == number:
                    search = True
                    
                elif search and number > num:
                    found = True
                    tresor.append(number)
                    break
                
            if not found:
                tresor.append(-1)
                
        return tresor


s = Solution()
print(s.nextGreaterElement(nums1, nums2))
