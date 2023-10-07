

nums = [4,2,5,7]

class Solution(object):
    def sortArrayByParityII(self, nums):
        
        hashmap = {
            'odd': [],
            'even': [],
        }
        tresor = []
        
        for num in nums:
            if num % 2 == 0:
                hashmap['even'].append(num)
            else:
                hashmap['odd'].append(num)
        
        
        while hashmap['odd'] != [] and hashmap['even'] != []:
            
            even = hashmap['even'].pop()
            tresor.append(even)
            odd = hashmap['odd'].pop()
            tresor.append(odd)
            
        return tresor
            

solution = Solution()
print(solution.sortArrayByParityII(nums))

        