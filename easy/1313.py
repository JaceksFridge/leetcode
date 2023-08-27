

nums = [1, 2, 3, 4]

class Solution(object):
    def decompressRLElist(self, nums):
        master_list = []

        for i in range(0, len(nums), 2):
            master_list.extend([nums[i+1]] * nums[i])

        return master_list






sol = Solution()
print(sol.decompressRLElist(nums))
