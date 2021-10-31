#!/usr/bin/env python
import unittest
from typing import List


"""
正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return []


def helper(
    nums: List[int],
    length: int,
    i: int,
    ret: List[List[int]],
) -> List[List[int]]:
    if length == i:
        ret.append(list(nums))
    elif i < length:
        for j in range(i, length):
            nums[i], nums[j] = nums[j], nums[i]
            ret = helper(nums, length, i + 1, ret)
            nums[i], nums[j] = nums[j], nums[i]
    return ret


cases = [
    {
        "input": [3],
        "output": ["((()))", "(()())", "(())()", "()(())", "()()()"],
    },
    {"input": [1], "output": ["()"]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().generateParenthesis(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
