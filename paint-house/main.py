#!/usr/bin/env python
import unittest
from typing import List


"""
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵
costs 来表示的。
例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。

请计算出粉刷完所有房子最少的花费成本。

示例 1：

输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
     最少花费: 2 + 5 + 3 = 10。
示例 2：

输入: costs = [[7,6,2]]
输出: 2
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        i = costs[0].index(max(costs[0]))
        dp = [[0] * 3 for _ in range(len(costs))]
        return min(
            helper(costs, dp, 0, (i + 1) % 3),
            helper(costs, dp, 0, (i + 2) % 3),
        )


def helper(costs: List[List[int]], dp: List[List[int]], i: int, j: int) -> int:
    if i < len(costs):
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = (
            min(
                helper(costs, dp, i + 1, (j + 1) % 3),
                helper(costs, dp, i + 1, (j + 2) % 3),
            )
            + costs[i][j]
        )
        return dp[i][j]
    return 0


# def helper(costs):
#     if not costs:
#         return 0
#     n = len(costs)
#     dp = [[0] * 3 for _ in range(n)]
#     dp[0] = costs[0]
#     for i in range(1, n):
#         for j in range(3):
#             dp[i][j] = (
#                 min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
#                 + costs[i][j]
#             )
#     return min(dp[n - 1])


cases = [
    {"input": [[[17, 2, 17], [16, 16, 5], [14, 3, 19]]], "output": 10},
    {"input": [[[7, 6, 2]]], "output": 2},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().minCost(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
