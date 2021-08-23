#!/usr/bin/env python3
from collections import defaultdict, deque
from typing import Dict, List
import unittest


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph: Dict[int, int] = {x: [] for x in range(vertices)}

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)


class SolutionDFS:
    def findCourseOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        g = Graph(numCourses)
        for u, v in prerequisites:
            if v not in g.graph[u]:
                g.add_edge(u, v)
        visited = {x: False for x in g.graph}
        path = []
        for v in g.graph:
            if not visited[v]:
                self.util(v, visited, path, g)
        return path

    def util(self, v: int, visited: Dict[int, bool], path: List[int], g: Graph):
        visited[v] = True
        for i in g.graph[v]:
            if not visited[i]:
                self.util(i, visited, path, g)
        path.append(v)


class Solution:
    def findCourseOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        indegrees = [0] * numCourses
        edge = [[] for _ in range(numCourses)]
        queue = []
        path = []
        for u, v in prerequisites:
            indegrees[u] += 1
            edge[v].append(u)
        [queue.append(i) for i, v in enumerate(indegrees) if not v]
        self.util(queue, path, edge, indegrees)
        if len(path) != numCourses:
            return []
        return path

    def util(self, queue, path, edge, indegrees):
        if not queue:
            return
        head = queue.pop()
        path.append(head)
        for x in edge[head]:
            indegrees[x] -= 1
            if not indegrees[x]:
                queue.append(x)
        self.util(queue, path, edge, indegrees)




class CourseTestCase(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(Solution().findCourseOrder(2, [[1, 0]]), [0, 1])

        self.assertEqual(Solution().findCourseOrder(2, [[1, 0]]), [0, 1])

        self.assertEqual(
            Solution().findCourseOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            [0, 2, 1, 3],
        )

        self.assertEqual(Solution().findCourseOrder(1, []), [0])
        self.assertEqual(Solution().findCourseOrder(2, []), [1, 0])
        self.assertEqual(Solution().findCourseOrder(2, [[0, 1], [1, 0]]), [])


if __name__ == "__main__":
    unittest.main()
