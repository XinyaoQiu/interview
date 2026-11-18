class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_nodes(root):
    out, stack, node = [], [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node)
        node = node.right
    return out


def bt_to_bst(root):
    nodes = inorder_nodes(root)
    for node, val in zip(nodes, sorted(n.val for n in nodes)):
        node.val = val
    return root


# follow-up: O(1) extra space, Morris inorder + bubble sort on values, O(n^2) time
def bt_to_bst_morris(root):
    swapped = True
    while swapped:
        swapped = False
        prev = None
        cur = root
        while cur:
            if cur.left:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                    continue
                pred.right = None
            if prev and prev.val > cur.val:
                prev.val, cur.val = cur.val, prev.val
                swapped = True
            prev = cur
            cur = cur.right
    return root


# follow-up: build a new BST with the same shape, original tree untouched
def build_new_bst(root):
    vals = iter(sorted(n.val for n in inorder_nodes(root)))

    def clone(node):
        if not node:
            return None
        left = clone(node.left)
        new = TreeNode(next(vals), left)
        new.right = clone(node.right)
        return new

    return clone(root)


def inorder_vals(root):
    return [n.val for n in inorder_nodes(root)]


def preorder_vals(root):
    return [] if not root else [root.val] + preorder_vals(root.left) + preorder_vals(root.right)


def is_bst(root, lo=float("-inf"), hi=float("inf")):
    if not root:
        return True
    return lo <= root.val <= hi and is_bst(root.left, lo, root.val) and is_bst(root.right, root.val, hi)


#        10
#       /  \
#      2    7
#     / \
#    8   4
t = TreeNode(10, TreeNode(2, TreeNode(8), TreeNode(4)), TreeNode(7))
print(preorder_vals(t), is_bst(t))
bt_to_bst(t)
print(preorder_vals(t), inorder_vals(t), is_bst(t))

t2 = TreeNode(10, TreeNode(2, TreeNode(8), TreeNode(4)), TreeNode(7))
new = build_new_bst(t2)
print(preorder_vals(new), inorder_vals(new), is_bst(new))
print(preorder_vals(t2))

t3 = TreeNode(10, TreeNode(2, TreeNode(8), TreeNode(4)), TreeNode(7))
bt_to_bst_morris(t3)
print(preorder_vals(t3), inorder_vals(t3), is_bst(t3))

t4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, TreeNode(9), TreeNode(0))))
print(preorder_vals(bt_to_bst_morris(t4)), is_bst(t4))

print(preorder_vals(bt_to_bst(None)), preorder_vals(build_new_bst(None)), preorder_vals(bt_to_bst_morris(None)))
print(preorder_vals(bt_to_bst(TreeNode(5))))
