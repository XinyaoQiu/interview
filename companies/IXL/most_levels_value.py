from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def most_levels_value(root):
    if not root:
        return []
    level_count = {}
    q = deque([root])
    while q:
        seen = {}
        for _ in range(len(q)):
            node = q.popleft()
            seen[node.val] = None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        for val in seen:
            level_count[val] = level_count.get(val, 0) + 1
    best = max(level_count.values())
    return [val for val, cnt in level_count.items() if cnt == best]


#       A
#      / \
#     A   B
#    / \
#   C   C
t = TreeNode("A", TreeNode("A", TreeNode("C"), TreeNode("C")), TreeNode("B"))
print(most_levels_value(t))

print(most_levels_value(None))
print(most_levels_value(TreeNode("X")))

#       A
#      / \
#     B   B
#    /     \
#   C       B
t2 = TreeNode("A", TreeNode("B", TreeNode("C")), TreeNode("B", None, TreeNode("B")))
print(most_levels_value(t2))

#   A
#    \
#     C
#      \
#       C
#        \
#         A
#          \
#           A
t3 = TreeNode("A", None, TreeNode("C", None, TreeNode("C", None, TreeNode("A", None, TreeNode("A")))))
print(most_levels_value(t3))

#       A
#      / \
#     B   C
#    /     \
#   B       C
t4 = TreeNode("A", TreeNode("B", TreeNode("B")), TreeNode("C", None, TreeNode("C")))
print(most_levels_value(t4))
