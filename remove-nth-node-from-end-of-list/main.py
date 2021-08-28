#!/usr/bin/env python
import unittest
from typing import List


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
class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def append(self, val: int) -> "ListNode":
        dummy = ListNode(-1, self)
        head = dummy
        node = ListNode(val)
        while head.next:
            head = head.next
        head.next = node
        return dummy.next

    def delete(self, val):
        dummy = ListNode(-1, self)
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return dummy.next

    def pop(self):
        dummy = ListNode(-1, self)
        node = dummy
        while node.next:
            if not node.next.next:
                node.next = None
                break
            node = node.next
        return dummy.next

    def toList(self) -> List[int]:
        if self.val is None:
            return []
        ret = [self.val]
        node = self.next
        while node:
            ret.append(node.val)
            node = node.next
        return ret

    @classmethod
    def fromList(cls, data: List[int]) -> "ListNode":
        dummy = ListNode(-1)
        node = dummy
        for _ in data:
            node.next = cls(_)
            node = node.next
        return dummy.next


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
