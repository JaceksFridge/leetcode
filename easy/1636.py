

nums = [1,1,2,2,2,3]

class Solution(object):
    def frequencySort(self, nums):
        
        
        hashmap = {}
        
        for num in nums:
            
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        
        hashsort = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        print(hashsort)

sol = Solution()
print(sol.frequencySort(nums))
