#!/usr/bin/env python
import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a = (a ^ n) & ~b
            b = (b ^ n) & ~a
        return a


cases = [
    {"input": [[2, 2, 3, 2]], "output": 3},
    {"input": [[0, 1, 0, 1, 0, 1, 100]], "output": 100},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().singleNumber(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
