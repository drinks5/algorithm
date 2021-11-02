#!/usr/bin/env python
import unittest
from typing import List


"""
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。

请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

示例 1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
"""


class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     i = len(cost)
    #     dp = [0] * i
    #     return min(helper(cost, dp, i - 2), helper(cost, dp, i - 1))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            dp[i % 2] = min(dp[0], dp[1]) + cost[i]
        return min(dp[0], dp[-1])


def helper(cost: List[int], dp: List[int], i: int) -> int:
    if i < 2:
        dp[i] = cost[i]
        return cost[i]
    if dp[i] == 0:
        dp[i] = min(helper(cost, dp, i - 2), helper(cost, dp, i - 1)) + cost[i]
    return dp[i]


cases = [
    {"input": [[10, 15, 20]], "output": 15},
    {"input": [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]], "output": 6},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().minCostClimbingStairs(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
