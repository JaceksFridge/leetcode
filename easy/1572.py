



mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]



class Solution(object):
    def diagonalSum(self, mat):

        
        sum = 0
        for i, row in enumerate(mat):
            
            if i == len(mat) -i -1:
                sum += row[i]
            else:
                sum += row[i]
                sum += row[-i -1]
            
        return sum
s = Solution()
print(s.diagonalSum(mat))    