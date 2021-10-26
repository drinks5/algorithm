#!/usr/bin/env python
import unittest


"""
给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。

正数的平方根有两个，只输出其中的正数平方根。

如果平方根不是整数，输出只保留整数的部分，小数部分将被舍去。

示例 1:

输入: x = 4
输出: 2
示例 2:

输入: x = 8
输出: 2
解释: 8 的平方根是 2.82842...，由于小数部分将被舍去，所以返回 2
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        low, high = 0, x
        mid = low + ((high - low) >> 1)
        while (high - low) > 1:
            ans = mid * mid
            if ans > x:
                high = mid
            elif ans < x:
                low = mid
            else:
                return mid
            mid = low + ((high - low) >> 1)
        return mid


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [1], "output": 1},
            {"input": [4], "output": 2},
            {"input": [8], "output": 2},
            {"input": [16], "output": 4},
            {"input": [25], "output": 5},
            {"input": [26], "output": 5},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().mySqrt(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
