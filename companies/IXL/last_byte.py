def last_byte_len_forward(data):
    i = 0
    length = 0
    while i < len(data):
        length = 2 if data[i] >= 128 else 1
        i += length
    return length


def last_byte_len(data):
    n = len(data)
    if n == 1:
        return 1
    if data[-1] >= 128:
        return 2
    count = 0
    i = n - 2
    while i >= 0 and data[i] >= 128:
        count += 1
        i -= 1
    return 2 if count % 2 else 1


tests = [
    [1, 200, 200, 126],
    [1, 3, 200, 200, 200, 200],
    [1, 200, 200, 200, 1, 1],
    [1, 200, 200, 200, 1],
    [5],
    [200, 5],
    [127, 127],
    [128, 127],
    [200, 200, 200, 200, 200, 5],
    [200, 200, 200, 200, 5],
]
for t in tests:
    print(t, last_byte_len(t), last_byte_len_forward(t))
