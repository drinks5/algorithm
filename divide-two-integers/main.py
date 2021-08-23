#,!/usr/bin/env python
import unittest


"""
9 /3 = 9/(2+1) = 9 >> 1 - 1
7 / -2 = 7 >> 1 = -2
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        return 1
        if not a:
            return 0
        sign = a ^ b >= 0
        left, right = abs(a), abs(b)
        return count

    def add(self, a: int, b: int) -> int:
        if not b:
            return a
        return self.add(a ^ b, (a & b) << 1)

    def negtive(self, n: int) -> int:
        return self.add(~n, 1)

    def sub(self, a: int, b: int) -> int:
        return self.add(a, self.negtive(b))


def add(a, b):
    if not b:
        return a
    return add(a ^ b, (a & b) << 1)


class SolutionTestCase(unittest.TestCase):
    def test_add(self):
        table = [
            {"input": [15, 2], "output": 17},
            {"input": [1, 1], "output": 2},
            {"input": [0, 1], "output": 1},
            # {"input": [7, -3], "output": 4},
            # 这个case会位溢出
        ]
        for t in table:
            self.assertEqual(add(*t["input"]), t["output"])

    def test_sub(self):
        table = [
            {"input": [15, 2], "output": 13},
            {"input": [1, 1], "output": 0},
            {"input": [0, 1], "output": -1},
            # {"input": [7, -3], "output": 10},
        ]
        for t in table:
            self.assertEqual(Solution().sub(*t["input"]), t["output"])

    def test_divide(self):
        table = [
            {"input": [15, 2], "output": 7},
            {"input": [1, 1], "output": 1},
            {"input": [0, 1], "output": 0},
            # {"input": [7, -3], "output": -2},
        ]
        for t in table:
            self.assertEqual(Solution().divide(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
