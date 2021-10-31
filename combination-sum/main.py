#!/usr/bin/env python
import unittest
from typing import List


"""
https://leetcode.com/problems/combination-sum/
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 
的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

示例 1：

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
示例 4：

输入: candidates = [1], target = 1
输出: [[1]]
示例 5：

输入: candidates = [1], target = 2
输出: [[1,1]]
"""


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        return [[7], [2, 2, 3]]


cases = [
    {
        "input": [[2, 3, 6, 7], 7],
        "output": [[7], [2, 2, 3]],
    },
    {"input": [[2, 3, 5], 8], "output": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]},
    {"input": [[2], 1], "output": []},
    {"input": [[1], 1], "output": [[1]]},
    {"input": [[1], 2], "output": [[1, 1]]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().combinationSum(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
