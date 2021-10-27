#!/usr/bin/env python3
from typing import Dict, List
import unittest

"""
现在总共有 numCourses 门课需要选，记为 0 到 numCourses-1。

给定一个数组 prerequisites ，它的每一个元素 prerequisites[i] 表示两门课程之间的先修顺序。 例如 prerequisites[i] = [ai, bi] 表示想要学习课程 ai ，需要先完成课程 bi 。

请根据给出的总课程数  numCourses 和表示先修顺序的 prerequisites 得出一个可行的修课序列。

可能会有多个正确的顺序，只要任意返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: numCourses = 2, prerequisites = [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
示例 3:

输入: numCourses = 1, prerequisites = [] 
输出: [0]
解释: 总共 1 门课，直接修第一门课就可。

提示:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
prerequisites 中不存在重复元素
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph: Dict[int, List[int]] = {x: [] for x in range(vertices)}

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


cases = [
    {"input": [2, [[1, 0]]], "output": [0, 1]},
    {"input": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], "output": [0, 2, 1, 3]},
    {"input": [1, []], "output": [0]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().findCourseOrder(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
