import heapq


from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(N log k) where N is total nodes and k the number of lists.
    # Space: O(k) for the heap.
    # Idea: keep the head of every list in a min-heap and pop the smallest.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i, head in enumerate(lists):
            if head:
                heap.append((head.val, i, head))
        heapq.heapify(heap)
        dummy = ListNode()
        cur = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            nxt = node.next
            if nxt:
                heapq.heappush(heap, (nxt.val, i, nxt))
        return dummy.next


def build(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()
    res = sol.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])
    assert to_list(res) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("basic ok")
