#!/usr/bin/env python
import unittest
from typing import List
import random


"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.sample(nums, 1)[0]
        larger = [n for n in nums if n > pivot]
        smaller = [n for n in nums if n < pivot]
        equal = [n for n in nums if n == pivot]

        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif len(larger) + len(equal) >= k:
            return pivot
        else:
            return self.findKthLargest(smaller + equal, k - len(larger))


cases = [
    {
        "input": [[3, 2, 1, 5, 6, 4], 2],
        "output": 5,
    },
    {
        "input": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
        "output": 4,
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().findKthLargest(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
