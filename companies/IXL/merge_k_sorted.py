import heapq


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_two_lists(a, b):
    dummy = tail = ListNode(0)
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def merge_k_lists_heap(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode(0)
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def merge_k_lists_pairwise(lists):
    if not lists:
        return None
    lists = list(lists)
    step = 1
    while step < len(lists):
        for i in range(0, len(lists) - step, step * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + step])
        step *= 2
    return lists[0]


def merge_two_arrays(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


def merge_k_arrays(arrays):
    heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]
    heapq.heapify(heap)
    out = []
    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)
        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))
    return out


def merge_k_iterators(iterators):
    done = object()
    heap = []
    for i, it in enumerate(iterators):
        val = next(it, done)
        if val is not done:
            heap.append((val, i, it))
    heapq.heapify(heap)
    while heap:
        val, i, it = heap[0]
        yield val
        nxt = next(it, done)
        if nxt is done:
            heapq.heappop(heap)
        else:
            heapq.heapreplace(heap, (nxt, i, it))


def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second, slow.next = slow.next, None
    return merge_two_lists(sort_list(head), sort_list(second))


def merge_k_unsorted_lists(lists):
    return merge_k_lists_pairwise([sort_list(h) for h in lists])


def build(vals):
    dummy = tail = ListNode(0)
    for v in vals:
        tail.next = tail = ListNode(v)
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


print(to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))))
print(to_list(merge_two_lists(build([]), build([0]))))

print(to_list(merge_k_lists_heap([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))
print(to_list(merge_k_lists_heap([])))
print(to_list(merge_k_lists_heap([build([]), build([])])))

print(to_list(merge_k_lists_pairwise([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))
print(to_list(merge_k_lists_pairwise([build([5]), build([3]), build([4]), build([1]), build([2])])))
print(to_list(merge_k_lists_pairwise([])))

print(merge_two_arrays([1, 2, 4], [1, 3, 4]))
print(merge_k_arrays([[1, 4, 5], [1, 3, 4], [2, 6]]))
print(merge_k_arrays([[], [7], []]))

print(list(merge_k_iterators([iter([1, 4, 5]), iter([1, 3, 4]), iter([2, 6])])))
print(list(merge_k_iterators([iter([]), iter([0, 0]), iter([])])))
print(list(merge_k_iterators([])))
squares = (x * x for x in range(1, 5))
odds = (x for x in range(1, 10, 2))
print(list(merge_k_iterators([squares, odds])))
gen = merge_k_iterators([iter(range(0, 10**9, 2)), iter(range(1, 10**9, 2))])
print([next(gen) for _ in range(6)])

print(to_list(merge_k_unsorted_lists([build([5, 1, 4]), build([3, 1]), build([6, 2, 2])])))
