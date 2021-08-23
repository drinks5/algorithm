#!/usr/bin/env python
import unittest
from typing import Dict, List


"""
把区间转换为比特位，如果a，b两个区间有重叠，则 a & b !=0
否则 a & b == 0
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        bitNums = []
        intervals.sort(key=lambda x: x[0])
        for nums in intervals:
            bit = 0
            for x in range(nums[0], nums[1] + 1):
                bit |= 1 << x
            bitNums.append((bit, nums))
        i = 1
        ans = [bitNums[0]]
        while i < len(bitNums):
            pre, pre_value = bitNums[i]
            current, current_value = ans[-1]
            if (pre & current) == 0:
                ans.append(bitNums[i])
            else:
                min_value, max_value = min(*pre_value, *current_value), max(
                    *pre_value, *current_value
                )
                pre = 0
                for x in range(min_value, max_value + 1):
                    pre |= 1 << x
                pre_value = [min_value, max_value]
                ans[-1] = (pre, pre_value)
            i += 1
        return [x[1] for x in ans]

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        bitNums = []
        for nums in intervals:
            bit = 0
            for x in range(nums[0], nums[1] + 1):
                bit |= 1 << x
            bitNums.append((bit, nums))
        length = len(nums)
        for i in range(length):


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            # {"input": ["11", "10"], "output": "101"},
            # {"input": ["1010", "1011"], "output": "10101"},
            # {"input": ["1", "111"], "output": "1000"},
            {
                "input": [[1, 3], [2, 6], [8, 10], [15, 18]],
                "output": [[1, 6], [8, 10], [15, 18]],
            },
            {"input": [[1, 4], [4, 5]], "output": [[1, 5]]},
            {"input": [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], "output": [[1, 10]]},
        ]
        for t in table:
            self.assertListEqual(Solution().merge(t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
