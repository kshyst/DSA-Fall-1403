from collections import deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = Graph()

        for i in range(len(arr)):
            graph.add(i)

        added_numbers = dict(set())

        for i in range(len(arr)):
            if arr[i] not in added_numbers:
                added_numbers.update({arr[i]: set()})
            for j in added_numbers[arr[i]]:
                graph.add_edge(j, i)
            added_numbers[arr[i]].add(i)

            if i > 0:
                graph.add_edge(i, i - 1)
            if i < len(arr) - 1:
                graph.add_edge(i, i + 1)

        #print(added_numbers)
        #print(graph)
        v = self.bfs(graph)

        if v is None:
            return 0
        return v

    def bfs(self, graph: dict) -> int:

        q = deque()
        visited = [False] * len(graph)

        visited[0] = True
        q.append(0)

        vertices = dict({0: 0})

        while q:

            curr = q.popleft()
            #print(curr, end=" ")

            for i in graph[curr]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    if i == len(graph) - 1:
                        return vertices[curr] + 1
                    vertices.update({i: vertices[curr] + 1})


class Graph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)
        self[v].add(u)

    def add_edge_set(self, v: int, s: set):
        self

    def delete_v(self, v):
        self.pop(self[v])


x = Solution()

print(x.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
