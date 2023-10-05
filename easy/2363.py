

from collections import defaultdict

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
           
        hashmap = defaultdict()
        tresor = []
        
         
        superitem = items1 + items2
        for item in superitem:
            hashmap[item[0]] = hashmap.get(item[0], 0) + item[1]
            
            
        for item in sorted(hashmap):
            tresor.append([ item, hashmap[item] ])
            
        return tresor
       

s = Solution()
print(s.mergeSimilarItems(items1, items2))

        