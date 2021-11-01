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
[-3,-2,-1,1,2,3]
[-3,-2,2,-1,1,3]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return helper(n, n, "", [])


def helper(
    left: int,
    right: int,
    parentThesis: str,
    ret: List[str],
) -> List[str]:
    if not left and not right:
        ret.append(parentThesis)
        return ret
    if left > 0:
        ret = helper(left - 1, right, parentThesis + "(", ret)
    if left < right:
        ret = helper(left, right - 1, parentThesis + ")", ret)
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
