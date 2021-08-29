#!/usr/bin/env python
import unittest
from typing import List
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


"""
给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

进阶：能尝试使用一趟扫描实现吗？

链接：https://leetcode-cn.com/problems/SLwz0R
"""


# Definition for singly-linked list.
class Solution:
    def call(self, data: List[int], k: int) -> List[int]:
        head = self.removeNthFromEnd(ListNode.fromList(data), k)
        return head and head.toList() or []

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        front, back = head, dummy
        for i in range(n):
            front = front.next
            # if front is None:
            #     return dummy.next
        while front is not None:
            front = front.next
            back = back.next
        back.next = back.next.next
        return dummy.next


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 2, 3, 4, 5], 2], "output": [1, 2, 3, 5]},
            {"input": [[1, 2], 1], "output": [1]},
            {"input": [[1], 1], "output": []},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
