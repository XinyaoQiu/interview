from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Idea: find the node where the cycle begins in a linked list, or None.
# Floyd's algorithm. If the head-to-cycle distance is a and the meeting point is
# b steps into the cycle, then a == (cycle length - b) mod cycle length, so
# walking from head and from the meeting point at the same speed meets at the start.
# Time: O(n), Space: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # reset slow to head; both now move one step at a time
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


def build(vals, pos):
    """Build a list from vals; tail connects to index pos (-1 for no cycle)."""
    nodes = [ListNode(v) for v in vals]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes


if __name__ == "__main__":
    s = Solution()
    nodes = build([3, 2, 0, -4], 1)
    assert s.detectCycle(nodes[0]) is nodes[1]
    nodes = build([1, 2], 0)
    assert s.detectCycle(nodes[0]) is nodes[0]
    nodes = build([1], -1)
    assert s.detectCycle(nodes[0]) is None
    assert s.detectCycle(None) is None
    nodes = build([1], 0)
    assert s.detectCycle(nodes[0]) is nodes[0]
    nodes = build([1, 2, 3, 4, 5], -1)
    assert s.detectCycle(nodes[0]) is None
    nodes = build(list(range(100)), 57)
    assert s.detectCycle(nodes[0]) is nodes[57]
    print("all tests passed")
