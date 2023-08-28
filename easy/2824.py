

nums = [-6,2,5,-2,-7,-1,3]
target = -2

# [-2, -1]
class Solution(object):
    def countPairs(self, nums, target):



        nums = sorted(nums, reverse=False)
        
        counter = 0
        p1 = 0
        p2 = len(nums) - 1
        
        while p1 < p2:

            if (nums[p1] + nums[p2]) < target:
                counter += p2 - p1
                p1 += 1
            else:
                p2 -= 1
        return counter
                





sol = Solution()
print(sol.countPairs(nums, target))

