

class Solution(object):
    def divideArray(self, nums):

        hashmap = { }

        for i, num in enumerate(nums):

            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        
        for k, v in hashmap.items():
            if v % 2 != 0:
                return False
        return True
