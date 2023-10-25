

root = [1,2,2,3,3,None,None,4,4]

class Solution(object):
    def isBalanced(self, root):
        
        for i in range(len(root)):
            
            arr = []
            arr.append(root[i])
                 
            if len(arr) == 2:
                if not arr[0] and type(arr[1]) == int:
                    return False
                elif not arr[1] and type(arr[0]) == int:
                    return False

                arr = []

        return True
        
s = Solution()
print(s.isBalanced(root))
