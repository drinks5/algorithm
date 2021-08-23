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
        """"""


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        pass
        # table = [
        #     # {"input": ["11", "10"], "output": "101"},
        #     # {"input": ["1010", "1011"], "output": "10101"},
        #     # {"input": ["1", "111"], "output": "1000"},
        #     {"input": ["100", "110010"], "output": "110110"},
        # ]
        # for t in table:
        #     self.assertEqual(Solution().addBinaryDFS(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
