

class Solution:
    def countDigits(self, num: int) -> int:

        nums = str(num)
        nums = list(nums)
        counter = 0
        
        for x in nums:
            x = int(x)
            if num % x == 0:
                counter += 1

        return counter