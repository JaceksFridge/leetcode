

class Solution(object):
    def diameterOfBinaryTree(self, root):
        max_diameter = [0]

        def height(node):

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            max_diameter[0] = max(max_diameter[0], left_height + right_height)

            return max(left_height, right_height) + 1

        height(root)
        return max_diameter[0]
