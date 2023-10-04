

nums = [-1,-2,-3,-4,3,2,1]


def signFunc(x):
        
    number = 1
    for i in x:
        if i < 0:
            number *= -1
        elif i == 0:
            return 0
    return number


class Solution(object):
    def arraySign(self, nums):
        
        return signFunc(nums)


sol = Solution()
sol.arraySign(nums)