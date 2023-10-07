

nums1 = [4,1,2]
nums2 = [1,3,4,2]



class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        
        hashmap = {}
        stack = []
        tresor = [-1] * len(nums1)
        
        for i, val in enumerate(nums1):
            hashmap[val] = i
        
        for idx, num in enumerate(nums2):
            while stack and num > stack[-1]:
                value = stack.pop()
                index = hashmap[value]
                tresor[index] = num
            if num in nums1:
                stack.append(num)
        return tresor
        
        

s = Solution()
s.nextGreaterElement(nums1, nums2)



# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
        
#         tresor = []
        
#         for num in nums1:
            
#             search = False
#             found = False
            
#             for number in nums2:
                
#                 if num == number:
#                     search = True
                    
#                 elif search and number > num:
#                     found = True
#                     tresor.append(number)
#                     break
                
#             if not found:
#                 tresor.append(-1)
                
#         return tresor


# s = Solution()
# s.nextGreaterElement(nums1, nums2)
