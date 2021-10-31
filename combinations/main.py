#!/usr/bin/env python
import unittest
from typing import List


"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例 1:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2:

输入: n = 1, k = 1
输出: [[1]]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return []
        nums = list(range(1, n + 1))
        return helper(nums, 0, [], [], k)


def helper(
    nums: List[int],
    index: int,
    subset: List[int],
    ret: List[List[int]],
    k: int,
) -> List[List[int]]:
    if len(subset) == k:
        ret.append(list(subset))
        return ret
    if index >= len(nums):
        return ret
    ret = helper(nums, index + 1, subset, ret, k)
    subset.append(nums[index])
    ret = helper(nums, index + 1, subset, ret, k)
    subset.pop()
    return ret


cases = [
    {
        "input": [4, 2],
        "output": [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().combine(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
