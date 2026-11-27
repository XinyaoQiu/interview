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
        best = 0

        def depth(node):
            nonlocal best
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)

        depth(root)
        return best
