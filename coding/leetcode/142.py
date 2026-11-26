from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Idea: find the node where the cycle begins in a linked list, or None.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        seen = set()
        node = head
        while node:
            if node in seen:
                return node
            seen.add(node)
            node = node.next
        return None
