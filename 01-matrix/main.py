#!/usr/bin/env python
import unittest
from typing import List, Tuple


"""
https://leetcode.com/problems/01-matrix/
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1：

输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
示例 2：

输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
"""
Dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if not rows:
            return []
        cols = len(mat[0])
        dists = [[0] * cols for _ in range(rows)]
        stack: List[Tuple[int, int]] = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dists[i][j] = 0
                    stack.append((i, j))
                else:
                    dists[i][j] = -1
        while stack:
            i, j= stack.pop()
            dist = dists[i][j]
            for d in Dirs:
                r = i+
        return []


cases = [
    {
        "input": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]],
        "output": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    },
    {
        "input": [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]],
        "output": [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().updateMatrix(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
