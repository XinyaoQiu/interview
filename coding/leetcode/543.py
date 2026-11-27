from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Idea: the diameter is the longest path between two nodes, measured in edges.
    # For every node, the longest path through it is left depth + right depth.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        def diameter(node):
            if node is None:
                return 0
            through = depth(node.left) + depth(node.right)
            return max(through, diameter(node.left), diameter(node.right))

        return diameter(root)
