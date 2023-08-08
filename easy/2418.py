

names = ["Mary","John","Emma"]
heights = [180,165,170]


class Solution:
    def sortPeople(self, names, heights):
        
        sum_list = []
        ret_list = []
        
        for x in range(len(names)):
            person = ( names[x], heights[x] )
            sum_list.append(person)
            
        sum_list.sort(key=lambda x: -x[1])
        
        for x in sum_list:
            ret_list.append(x[0])
            
        return ret_list

s = Solution()
print(s.sortPeople(names, heights))


# data.sort(key=lambda x: x[1])