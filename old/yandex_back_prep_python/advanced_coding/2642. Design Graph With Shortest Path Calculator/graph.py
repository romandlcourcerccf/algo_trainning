from typing import List

from collections import defaultdict

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self._edges = defaultdict(list)
        for edge in edges:
            self._edges[edge[0]].append(edge[1:])
        
    def addEdge(self, edge: List[int]):
        self._edges.append(edge)

    def shortestPath(self, node1: int, node2: int) -> int:
        
        stack = [node1]

        while stack:
            
        

