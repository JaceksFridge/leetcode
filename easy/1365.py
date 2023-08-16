

nums = [8,1,2,2,3]

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        score = []

        for i, n in enumerate(nums):

            counter = 0

            for j in range(len(nums)):
                print(f"i: {nums[i]}, j: {nums[j]}")

                if i == j:
                    pass
                elif nums[i] > nums[j]:
                    counter += 1

            score.append(counter)
        return score
    
    
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))
