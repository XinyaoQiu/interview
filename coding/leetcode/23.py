import heapq


from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Idea: keep the head of every list in a min-heap and pop the smallest.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        heapq.heapify(heap)
        dummy = ListNode()
        cur = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
