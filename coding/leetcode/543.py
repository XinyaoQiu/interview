from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Idea: the diameter is the longest path between two nodes, measured in edges.
    # For every node, the longest path through it is left depth + right depth.
    # Time: O(n), each node is visited once.
    # Space: O(h) recursion stack, h is the tree height (O(n) worst case).
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

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


if __name__ == "__main__":
    s = Solution()
    assert s.diameterOfBinaryTree(None) == 0
    assert s.diameterOfBinaryTree(TreeNode(1)) == 0
    assert s.diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
    t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.diameterOfBinaryTree(t) == 3
    # longest path that does not pass through the root
    t = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(6, None, TreeNode(7))))
    assert s.diameterOfBinaryTree(t) == 4
    print("all tests passed")
