#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import Dict, List
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


"""
给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。

示例 1：

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

链接：https://leetcode-cn.com/problems/UHnkqh
"""


class Solution:
    def call(self, l: List[int]) -> List[int]:
        node = self.reverseList(ListNode.fromList(l))
        return node and node.toList() or []

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 2, 3, 4, 5]], "output": [5, 4, 3, 2, 1]},
            {"input": [[1, 2]], "output": [2, 1]},
            {"input": [[]], "output": []},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
