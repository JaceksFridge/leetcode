

nums = [3,1,2,2,2,1,3]
k = 2

class Solution(object):
    def countPairs(self, nums, k):
        
        
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                if nums[i] != nums[j]:
                    continue
                if (i * j) % k != 0:
                    continue
                count += 1
        return count
        

s = Solution()
print(s.countPairs(nums, k))

        