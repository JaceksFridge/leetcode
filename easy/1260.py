

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

class Solution(object):
    def shiftGrid(self, grid, k):
        
        mega_list = []
        tresor = []
        row_length = len(grid[0])
        
        for row in grid:
            for num in row:
                mega_list.append(num)
        
        k = k % len(mega_list)
        mega_list = mega_list[-k:] + mega_list[:-k]


        for tripple in range(0, len(mega_list), row_length):
            row = []
            for num in range(row_length):
                row.append(mega_list[tripple + num])
            tresor.append(row)
        return tresor

s = Solution()
print(s.shiftGrid(grid, k))
