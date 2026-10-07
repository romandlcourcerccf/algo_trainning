from typing import List, Dict

graph = {
    "A": ["D", "F", "B"],
    "B": ["C"],
    "C": [],
    "D": ["E"],
    "E": ["G"],
    "F": [],
    "G": [],
}


# def dfs_iterative(start: str, graph: str) -> List[str]:
#     """
#     dfs iterative version.
#     """
#     stack = []
#     stack.append(start)
#     visited = []
#     num_visited = 0
#     while stack:
#         s = stack.pop()
#         num_visited += 1
#         visited.append((num_visited, s))

#         if s not in graph:
#             continue

#         for n in graph[s]:
#             stack.append(n)

#     print(visited)


# dfs_iterative("A", graph)


def dfs_iterative_search_path(
    start: str, end: str, graph: Dict[str, List[str]]
) -> List[str]:
    stack = []
    parent = {}

    stack.append(start)

    while stack:
        s = stack.pop()
        if s == end:
            path = []

            while s in parent.keys():
                path.insert(0, s)
                s = parent[s]

            path.insert(0, start)

            return path

        if s not in graph:
            continue

        for n in graph[s]:
            stack.append(n)
            parent[n] = s

    return []


print(dfs_iterative_search_path("A", "C", graph))
