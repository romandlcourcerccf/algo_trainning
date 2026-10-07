# graph = {
#     "a": set(["b", "c", "f"]),
#     "b": set(["a", "d", "f"]),
#     "c": set(["a", "f"]),
#     "d": set(["b", "g"]),
#     "e": set(["b", "f"]),
#     "g": set(["d"]),
#     "h": set(["c"]),
# }


# def dfs(self, start, end, graph):
#     stack, visited = [start], {}

#     while stack:
#         present = stack.pop()
#         visited.add(present)

#         if present in graph:
#             for node in self.tree[present]:
#                 if node == end:
#                     return visited
#                 if node not in visited and node not in stack:
#                     stack.append(node)

#     return {}


# print("path >>", dfs("a", "d", graph))

# print(graph)


# graph = {1: set([2, 3]), 2: set([4, 5]), 4: set([6, 7])}


# def dfs_iter(start, target, graph):
#     stack = [start]

#     while stack:
#         cur = stack.pop()
#         print(cur)
#         if cur == target:
#             return
#         if cur in graph:
#             for val in graph[cur]:
#                 stack.append(val)


# print(graph)

# dfs_iter(1, 4, graph)


tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": [],
}


# # Iterative DFS function
# def dfs_iterative(tree, start, target):
#     visited = set()  # Track visited nodes
#     stack = [start]  # Stack for DFS

#     while stack:  # Continue until stack is empty
#         node = stack.pop()  # Pop a node from the stack
#         if node not in visited:
#             visited.add(node)  # Mark node as visited
#             if node == target:
#                 return visited
#             print(node)  # Print the current node (for illustration)
#             stack.extend(reversed(tree[node]))  # Add child nodes to stack


# # Run DFS starting from node 'A'
# print(tree)

# print(dfs_iterative(tree, "A", "G"))


graph = {
    "A": ["D", "F", "B"],
    "B": ["C"],
    "C": [],
    "D": ["E"],
    "E": ["G"],
    "F": [],
    "G": [],
}


def dfs_non_recursive(graph, source, goal):
    path = []
    parent = {}

    stack = [source]

    while stack:
        s = stack.pop()

        if s == goal:
            path.append(goal)
            while s in parent.keys():
                path.append(parent[s])
                s = parent[s]
            return path[::-1]

        if s not in graph:
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)
            parent[neighbor] = s

    return path


DFS_path = dfs_non_recursive(graph, "A", "G")
print(DFS_path)
