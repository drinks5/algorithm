#!/usr/bin/env python
import unittest
from typing import List, Tuple


"""
https://leetcode.com/problems/max-area-of-island/
给定一个由 0 和 1 组成的非空二维数组 grid ，用来表示海洋岛屿地图。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        visited = [[False for y in range(cols)] for x in range(rows)]
        area = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] and not visited[i][j]:
                    a = getArea(grid, visited, (i, j), rows, cols)
                    area = max(a, area)
        return area


DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def getArea(
    grid: List[List[int]],
    visited: List[List[bool]],
    pos: Tuple[int, int],
    rows: int,
    cols: int,
) -> int:
    visited[pos[0]][pos[1]] = True
    stack: List[Tuple[int, int]] = [pos]
    area = 0
    while stack:
        area += 1
        i, j = stack.pop()
        for d in DIRS:
            r = i + d[0]
            c = j + d[1]
            if (
                0 <= r < rows
                and (0 <= c < cols)
                and (not visited[r][c])
                and (grid[r][c])
            ):
                stack.append((r, c))
                visited[r][c] = True
    return area


cases = [
    {
        "input": [
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        ],
        "output": 6,
    },
    {
        "input": [[[0, 0, 0, 0, 0, 0, 0, 0]]],
        "output": 0,
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().maxAreaOfIsland(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
