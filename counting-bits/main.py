#!/usr/bin/env python
import unittest
from typing import List


"""
偶数n可由n >> 1 得到，即偶数n与n/2 1的位数相同
如 6 = bits(110) = bits(11) = 3 相同
奇数 = n/2的位数+1
如 3 = 1 + bits(10)
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            {"input": [5], "output": [0, 1, 1, 2, 1, 2]},
        ]
        for t in table:
            self.assertListEqual(Solution().countBits(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
