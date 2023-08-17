

nums = [1,2,3,4,5]

class Solution(object):
    def sumOfUnique(self, nums):

        hashmap = {}
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        print(hashmap)
    
    
        sum = 0
        for num in nums:
            if hashmap[num] == 1:
                sum += num
        return sum
    
sol = Solution()
print(sol.sumOfUnique(nums))
