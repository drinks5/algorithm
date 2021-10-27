#!/usr/bin/env python
import unittest
from typing import List
import random


"""
https://leetcode-cn.com/problems/sort-list/
给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：

输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return None


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
