import heapq
import random


def assign_b_ids(msgs):
    c_pos = {}
    for i, m in enumerate(msgs):
        if m[0] == "C":
            c_pos[m[1:]] = i

    result = list(msgs)
    heap = []
    for i, m in enumerate(msgs):
        if m[0] == "A":
            cid = m[1:]
            heapq.heappush(heap, (c_pos.get(cid, float("inf")), cid))
        elif m == "B":
            if not heap:
                raise ValueError(f"no open A for B at index {i}")
            deadline, cid = heapq.heappop(heap)
            if deadline < i:
                raise ValueError(f"C{cid} already passed before B at index {i}")
            result[i] = "B" + cid
    return result


def validate(msgs, result, strict=True):
    if len(msgs) != len(result):
        return False
    a_pos, b_pos, c_pos = {}, {}, {}
    for i, (m, r) in enumerate(zip(msgs, result)):
        if m == "B":
            if r[0] != "B" or len(r) == 1 or r[1:] in b_pos:
                return False
            b_pos[r[1:]] = i
        elif m != r:
            return False
        elif m[0] == "A":
            a_pos[m[1:]] = i
        else:
            c_pos[m[1:]] = i
    for cid, b in b_pos.items():
        if cid not in a_pos or a_pos[cid] > b:
            return False
        if cid in c_pos and c_pos[cid] < b:
            return False
    if strict and set(a_pos) != set(b_pos):
        return False
    return True


def generate(n_clients, drop_rate=0.0, rng=random):
    slots = [None] * (3 * n_clients)
    order = list(range(3 * n_clients))
    rng.shuffle(order)
    for cid in range(1, n_clients + 1):
        a, b, c = sorted(order[3 * (cid - 1) : 3 * cid])
        dropped = rng.random() < drop_rate
        slots[a] = None if dropped else f"A{cid}"
        slots[b] = None if dropped else "B"
        slots[c] = f"C{cid}"
    return [m for m in slots if m is not None]


examples = [
    "A1 B A2 C1 B C2",
    "A2 A1 B C2 B C1",
    "A2 B A1 B C2 C1",
    "A1 A2 B B C1 C2",
    "A1 B C2 C1",
]
for e in examples:
    msgs = e.split()
    out = assign_b_ids(msgs)
    print(" ".join(out), validate(msgs, out))

try:
    assign_b_ids("A1 B B A2 C1 C2".split())
except ValueError as err:
    print("error:", err)

msgs = generate(4, rng=random.Random(1))
print(" ".join(msgs), "->", " ".join(assign_b_ids(msgs)))

rng = random.Random(10)
for _ in range(2000):
    msgs = generate(rng.randint(1, 12), rng=rng)
    assert validate(msgs, assign_b_ids(msgs))
print("2000 random complete logs valid")

for _ in range(2000):
    msgs = generate(rng.randint(1, 12), drop_rate=0.3, rng=rng)
    assert validate(msgs, assign_b_ids(msgs))
print("2000 random logs with missing A/B valid")
