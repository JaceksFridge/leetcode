

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

class Solution(object):
    def mergeTrees(self, root1, root2):
        


        if root1 and root2:
            merged_node = TreeNode(root1.val + root2.val)
            merged_node.left = self.mergeTrees(root1.left, root2.left)
            merged_node.right = self.mergeTrees(root1.right, root2.right)
            return merged_node
        else:
            return root1 or root2

s = Solution()
s.mergeTrees(root1, root2)