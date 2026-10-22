"""
Problem: Add Two Large Integers Represented by Linked Lists

Two large integers are stored in singly linked lists. Each node stores up to
4 decimal digits. Compute and output their sum.

Assumptions to confirm with the interviewer:
- Inputs represent nonnegative integers; each node value is between 0 and 9999.
- Both lists are nonempty and have no leading zero chunks.
  Zero is represented by a single node with value 0.
- The most significant chunk comes first. Every chunk after the first represents
  exactly 4 digits, padded with leading zeros. For example, 12 -> 3 means 120003.
- The input lists do not share nodes.
- Temporarily reversing the inputs is allowed, provided their original order
  is restored before returning.
- Return the sum in the same linked-list format.

Example:
    1234 -> 5678  +  8765 -> 4322
    Represents 12345678 + 87654322 = 100000000.
    Return 1 -> 0 -> 0, which prints as 100000000.

Approach: Reverse both lists to add chunks from the least significant end.
Each node acts as a base-10000 digit.
Use divmod(total, 10000) to compute the carry and the current result chunk.
Prepend each new node to keep the most significant chunk first.
Reverse both input lists again to restore their original order.
Do not convert either entire integer to a Python int.

Complexity: O(m + n) time and O(1) auxiliary space, excluding the result list.
The result list uses O(max(m, n)) space, where m and n are the input lengths.
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    previous = None
    while head:
        next_node = head.next
        head.next = previous
        previous = head
        head = next_node
    return previous


def add_large_numbers(first, second):
    reversed_first = reverse_list(first)
    reversed_second = reverse_list(second)
    left, right = reversed_first, reversed_second
    carry = 0
    head = None

    while left or right or carry:
        total = carry
        if left:
            total += left.val
            left = left.next
        if right:
            total += right.val
            right = right.next
        carry, chunk = divmod(total, 10000)
        head = ListNode(chunk, head)

    reverse_list(reversed_first)
    reverse_list(reversed_second)

    return head


def to_decimal_string(head):
    """Print the first chunk normally and pad every subsequent chunk to 4 digits."""
    parts = [str(head.val)]
    node = head.next
    while node:
        parts.append(f"{node.val:04d}")
        node = node.next
    return "".join(parts)


# Basic addition without a carry.
print(to_decimal_string(add_large_numbers(ListNode(1234), ListNode(4321))))  # 5555

# Carry into a new most significant chunk.
first = ListNode(1234, ListNode(5678))
second = ListNode(8765, ListNode(4322))
print(to_decimal_string(add_large_numbers(first, second)))  # 100000000
print(to_decimal_string(first))  # 12345678 (input restored)
print(to_decimal_string(second))  # 87654322 (input restored)

# Different lengths with a carry through multiple chunks.
first = ListNode(9999, ListNode(9999))
print(to_decimal_string(add_large_numbers(first, ListNode(1))))  # 100000000

# Pad lower chunks with leading zeros.
first = ListNode(12, ListNode(3))
print(to_decimal_string(add_large_numbers(first, ListNode(4))))  # 120007

# Zero.
print(to_decimal_string(add_large_numbers(ListNode(0), ListNode(0))))  # 0
