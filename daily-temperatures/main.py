#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import Dict, List


"""
请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]

提示：

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

链接：https://leetcode-cn.com/problems/iIQa4I
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return []


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {
                "input": [[73, 74, 75, 71, 69, 72, 76, 73]],
                "output": [1, 1, 4, 2, 1, 1, 0, 0],
            },
            {"input": [[30, 40, 50, 60]], "output": [1, 1, 1, 0]},
            {"input": [[30, 60, 90]], "output": [1, 1, 0]},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().dailyTemperatures(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
