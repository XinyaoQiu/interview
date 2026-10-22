"""
Problem: Find the Admin User

Each permission is a (source, relationship, destination) tuple:
- camera_owner: a user or group owns a camera.
- group_member: a user or group inherits permissions from the destination group.
Return the user who can access every camera, or None if no such user exists.
Return None if there are no cameras.

Assumptions to confirm with the interviewer:
- Input follows the stated entity prefixes and relationship formats.
- All organization cameras appear in camera_owner relationships.
- At most one user can access every camera.
- Groups may form cycles; duplicate relationships are allowed.

Approach: Build edges from each source to its destination. For each user,
run iterative DFS with a fresh visited set to handle cycles. The user is an
admin if every camera is reachable. Groups are never admin candidates.

Complexity: O(U * (V + E) + V + E) time and O(V + E) space,
where U is the number of users, V the number of entities, and E the number
of permission relationships.
"""

from collections import defaultdict


def find_admin_user(perms_data):
    graph = defaultdict(list)
    users = set()
    cameras = set()

    for source, relationship, destination in perms_data:
        graph[source].append(destination)
        if source.startswith("user_"):
            users.add(source)
        if relationship == "camera_owner":
            cameras.add(destination)

    if not cameras:
        return None

    for user in users:
        seen = set()
        stack = [user]

        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(graph.get(node, []))

        if cameras.issubset(seen):
            return user

    return None


# Direct ownership combined with inherited permissions.
print(find_admin_user([
    ("user_admin", "group_member", "group_sec"),
    ("group_sec", "camera_owner", "camera_1"),
    ("group_sec", "camera_owner", "camera_2"),
    ("user_admin", "camera_owner", "camera_3"),
    ("user_bob", "camera_owner", "camera_1"),
]))  # user_admin

# Nested groups.
print(find_admin_user([
    ("user_super", "group_member", "group_exec"),
    ("group_exec", "group_member", "group_ops"),
    ("group_ops", "camera_owner", "camera_hq"),
    ("user_super", "camera_owner", "camera_branch"),
]))  # user_super

# No single user owns every camera.
print(find_admin_user([
    ("user_alice", "camera_owner", "camera_1"),
    ("user_bob", "camera_owner", "camera_2"),
]))  # None

# Cyclic groups.
print(find_admin_user([
    ("user_admin", "group_member", "group_a"),
    ("group_a", "group_member", "group_b"),
    ("group_b", "group_member", "group_a"),
    ("group_a", "camera_owner", "camera_1"),
    ("group_b", "camera_owner", "camera_2"),
]))  # user_admin

# A group owns all cameras, but no user belongs to it.
print(find_admin_user([
    ("group_sec", "camera_owner", "camera_1"),
]))  # None

# No cameras.
print(find_admin_user([
    ("user_admin", "group_member", "group_sec"),
]))  # None
print(find_admin_user([]))  # None
