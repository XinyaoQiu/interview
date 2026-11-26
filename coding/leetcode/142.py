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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # restart one pointer from head; they meet at the cycle start
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
