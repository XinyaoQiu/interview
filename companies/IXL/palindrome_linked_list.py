class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return False

    second = reverse(slow)
    p, q = head, second
    result = True
    while q:
        if p.val != q.val:
            result = False
            break
        p, q = p.next, q.next
    reverse(second)
    return result


def build(vals, pos=-1):
    nodes = [ListNode(v) for v in vals]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


print(is_palindrome(build([1, 2, 2, 1])))
print(is_palindrome(build([1, 2, 3, 2, 1])))
print(is_palindrome(build([1, 2])))
print(is_palindrome(build([1])))
print(is_palindrome(build([])))
print(is_palindrome(build([1, 2, 3, 2, 1], pos=2)))
print(is_palindrome(build([1, 2, 2, 1], pos=0)))
print(is_palindrome(build([7], pos=0)))