

nums = [2,5,1,3,4,7]
n = 3

class Solution(object):
    def shuffle(self, nums, n):
        
        
        tresor = []
        
        arr1 = nums[:n]
        arr2 = nums[n:]
        

        for i in range(len(arr1)):
            tresor.append(arr1[i])
            tresor.append(arr2[i])
            
        return tresor
        
        
        
        
s = Solution()
print(s.shuffle(nums, n))

        
        

