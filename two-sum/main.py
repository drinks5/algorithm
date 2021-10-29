#!/usr/bin/env python
import unittest
from typing import List, Tuple


"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in counts:
                counts[n] = i
            else:
                return [counts[diff], i]
        return []


cases = [
    {
        "input": [[2, 7, 11, 15], 9],
        "output": [0, 1],
    },
    {
        "input": [[3, 2, 4], 6],
        "output": [1, 2],
    },
    {
        "input": [[3, 3], 6],
        "output": [0, 1],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().twoSum(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
