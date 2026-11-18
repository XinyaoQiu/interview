import heapq
from collections import defaultdict


def schedule(courses):
    indegree = {}
    priority = {}
    children = defaultdict(list)
    for cid, pri, deps in courses:
        priority[cid] = pri
        indegree[cid] = len(deps)
        for d in deps:
            children[d].append(cid)

    heap = [(-priority[c], c) for c in indegree if indegree[c] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        _, c = heapq.heappop(heap)
        order.append(c)
        for nxt in children[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(heap, (-priority[nxt], nxt))
    return order


print(schedule([[1, 5, [2]], [2, 0, []]]))
print(schedule([[1, 5, [2]], [2, 10, []], [3, 20, [1, 2]], [4, 0, [2]]]))
print(schedule([[1, 1, []], [2, 3, []], [3, 2, []]]))
print(schedule([[1, 7, []], [2, 7, []]]))
print(schedule([[1, 100, [2]], [2, 0, []], [3, 50, []]]))
print(schedule([]))
