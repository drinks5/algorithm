#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret: List[List[int]] = []
        if not nums:
            return ret
        helper(nums, 0, [], ret)
        return ret


def helper(
    nums: List[int], index: int, subset: List[int], result: List[List[int]]
):
    if index == len(nums):
        return result.append(list(subset))
    helper(nums, index + 1, subset, result)
    subset.append(nums[index])
    helper(nums, index + 1, subset, result)
    subset.pop()


cases = [
    {
        "input": [[1, 2, 3]],
        "output": [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]],
    },
    {"input": [[0]], "output": [[], [0]]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().subsets(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
