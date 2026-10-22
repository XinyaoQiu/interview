# Assume a dense n x n input, distinct matrix IDs, and positive batch/worker counts.
# The dictionary simulates external storage; calls simulate remote workers.


def read_batch(database, matrix_id, n, start, batch_size):
    records = []
    for index in range(start, min(start + batch_size, n * n)):
        row, col = divmod(index, n)
        records.append((row, col, database[matrix_id, row, col]))
    return records


def transpose_worker(records):
    # A worker receives only one batch, not the database or the full matrix.
    return [(col, row, value) for row, col, value in records]


def write_batch(database, matrix_id, records):
    for row, col, value in records:
        database[matrix_id, row, col] = value


def transpose(database, input_id, output_id, n, worker_count, batch_size):
    workers = [transpose_worker for _ in range(worker_count)]
    for batch_id, start in enumerate(range(0, n * n, batch_size)):
        records = read_batch(database, input_id, n, start, batch_size)
        worker = workers[batch_id % worker_count]
        result = worker(records)
        write_batch(database, output_id, result)
        # Finish this batch before reading another: O(batch_size) working memory.


# One dense 100 x 100 matrix; the output is stored under matrix ID 2.
n = 100
database = {(1, row, col): row * n + col + 1
            for row in range(n) for col in range(n)}
transpose(database, 1, 2, n, worker_count=4, batch_size=256)
print(sum(matrix_id == 2 for matrix_id, row, col in database))  # 10000
print(all(database[2, col, row] == database[1, row, col]
          for row in range(n) for col in range(n)))  # True


# Block-storage version: (matrix_id, block_row, block_col) -> 2D block.
# Assume separate input/output IDs and initially empty output storage.
# Storage occupies O(n^2); each worker needs O(block_size^2) working memory.


def read_block(database, matrix_id, block_row, block_col):
    return [row[:] for row in database[matrix_id, block_row, block_col]]


def write_block(database, matrix_id, block_row, block_col, block):
    database[matrix_id, block_row, block_col] = [row[:] for row in block]


def transpose_block_worker(block):
    # Only this block is visible to the worker. Edge blocks may be rectangular.
    return [[block[row][col] for row in range(len(block))]
            for col in range(len(block[0]))]


def transpose_blocks(database, input_id, output_id, n, block_size, worker_count):
    blocks_per_row = (n + block_size - 1) // block_size
    workers = [transpose_block_worker for _ in range(worker_count)]
    for task_id in range(blocks_per_row ** 2):
        block_row, block_col = divmod(task_id, blocks_per_row)
        block = read_block(database, input_id, block_row, block_col)
        result = workers[task_id % worker_count](block)
        write_block(database, output_id, block_col, block_row, result)
        # Sequential simulation: write this result before loading the next block.


# Generate input directly as 16 blocks, without building a full 2D matrix first.
size = 1000
block_size = 256
block_database = {}
for row in range(0, size, block_size):
    for col in range(0, size, block_size):
        block_database[1, row // block_size, col // block_size] = [
            [r * size + c + 1 for c in range(col, min(col + block_size, size))]
            for r in range(row, min(row + block_size, size))
        ]

transpose_blocks(block_database, 1, 2, size, block_size, worker_count=4)

# Compare every input cell with the corresponding output cell, block by block.
blocks_per_row = (size + block_size - 1) // block_size
print(sum(matrix_id == 2 for matrix_id, row, col in block_database))  # 16
print(all(
    block_database[2, bc, br][c][r] == value
    for br in range(blocks_per_row)
    for bc in range(blocks_per_row)
    for r, values in enumerate(block_database[1, br, bc])
    for c, value in enumerate(values)
))  # True
