#!/usr/bin/env python
import unittest
from typing import List


"""
一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一
晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 在不触动警报装置的情况下 ，今晚能够偷窃到的
最高金额。

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        return max(helper(nums[:-1]), helper(nums[1:]))


def helper(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[2] + nums[0]
    for i in range(3, len(nums)):
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
    return max(dp[-1], dp[-2], dp[-3])


cases = [
    {
        "input": [[1, 2, 1, 1]],
        "output": 3,
    },
    {
        "input": [[200, 3, 140, 20, 10]],
        "output": 340,
    },
    {
        "input": [[2, 3, 2]],
        "output": 3,
    },
    {
        "input": [[1, 2, 3, 1]],
        "output": 4,
    },
    {
        "input": [[0]],
        "output": 0,
    },
    {
        "input": [[1]],
        "output": 1,
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().rob(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
