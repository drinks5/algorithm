#!/usr/bin/env python
import unittest
from typing import List


"""
先遍历小的字符串
接着遍历小字符串到大字符串之间的 字符串
如
101, 10101
先遍历前三位
后遍历两位

"""


class Solution:
    def addBinaryDFS(self, a: str, b: str) -> str:
        if len(a) < len(b):
            min_str = a
            max_str = b
        else:
            min_str = b
            max_str = a
        ans: List[int] = []
        carry = self.util(min_str, max_str, -1, len(min_str), len(max_str), 0, ans)
        if carry > 0:
            ans.append(1)
        return "".join(map(str, ans[::-1]))

    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        if len(a) < len(b):
            min_str = a
            max_str = b
        else:
            min_str = b
            max_str = a

        for i in range(len(min_str) - 1, -1, -1):
            x = int(max_str[i - len(min_str)]) + int(min_str[i]) + carry
            if x >= 2:
                carry = 1
                x = x % 2
            else:
                carry = 0
            ans.append(x)
        for i in range(len(max_str) - len(min_str) - 1, -1, -1):
            x = int(max_str[i]) + carry
            if x >= 2:
                carry = 1
                x = x % 2
            else:
                carry = 0
            ans.append(x)
        if carry > 0:
            ans.append(1)
        return "".join(map(str, ans[::-1]))


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            # {"input": ["11", "10"], "output": "101"},
            # {"input": ["1010", "1011"], "output": "10101"},
            # {"input": ["1", "111"], "output": "1000"},
            {"input": ["100", "110010"], "output": "110110"},
        ]
        for t in table:
            self.assertEqual(Solution().addBinaryDFS(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
