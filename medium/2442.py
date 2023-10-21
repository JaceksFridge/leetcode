

nums = [1,13,10,12,31]

class Solution(object):
    def countDistinctIntegers(self, nums):
        
        
        numbers = set()

        for num in nums:
            numbers.add(num)
            numbers.add(int(str(num)[::-1]))
            
        return len(numbers)
        

        
s = Solution()
print(s.countDistinctIntegers(nums))
