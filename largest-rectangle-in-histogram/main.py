#!/usr/bin/env python
import unittest
from typing import Dict, List


"""
给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：

输入： heights = [2,4]
输出： 4
 
提示：

1 <= heights.length <=105
0 <= heights[i] <= 104

链接：https://leetcode-cn.com/problems/0ynMMM
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        """
        ret = 0
        stack = []
        for j, x in enumerate(heights):
            wide = 1
            height = x

        return 0


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[2, 4]], "output": 4},
            {"input": [[2, 1, 5, 6, 2, 3]], "output": 10},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().largestRectangleArea(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
