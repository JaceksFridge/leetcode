

numRows = 5

class Solution(object):
    def generate(self, numRows):
        
        
        numRows -= 1
        triangle= [ [1] ]
        

        for i in range(numRows):

            new_row  = [1]
            
            if len(triangle[i]) > 1:
                
                for j in range(1, len(triangle[i])):
                    new_row.append(triangle[i][j] + triangle[i][j-1])
            
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle
        
sol = Solution()
print(sol.generate(numRows))
