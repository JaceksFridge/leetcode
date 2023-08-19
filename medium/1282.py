

groupSizes = [3,3,3,3,3,1,3]

class Solution(object):
    def groupThePeople(self, groupSizes):

        hashmap = {}
        masterlist = []

        
        for i, num in enumerate(groupSizes):
            if num not in hashmap:
                hashmap[num] = []
            hashmap[num].append(i)


        for size, people in hashmap.items():
            for i in range(0 ,len(people), size):
                masterlist.append(people[i : i+size])
        


        return masterlist
        
        
sol = Solution()
print(sol.groupThePeople(groupSizes))
