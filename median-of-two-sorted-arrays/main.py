#!/usr/bin/env python3
import unittest
from typing import List

"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
"""


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        return 0


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 3], [2]], "output": 2},
            {"input": [[1, 3], [3, 4]], "output": 2.5},
            {"input": [[0, 0], [0, 0]], "output": 0},
            {"input": [[], []], "output": 1},
            {"input": [[2], []], "output": 2},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")

            self.assertEqual(
                Solution().findMedianSortedArrays(*t["input"]), t["output"]
            )


if __name__ == "__main__":
    unittest.main()
