#!/usr/bin/env python
import unittest
from typing import Dict, List, Optional


"""
给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例1：

输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
示例2：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
示例3：

输入：l1 = [0], l2 = [0]
输出：[0]
 
提示：

链表的长度范围为 [1, 100]
0 <= node.val <= 9
输入数据保证链表代表的数字无前导 0

进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。

链接：https://leetcode-cn.com/problems/lMSNwu
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
    def fromList(cls, data: List[int], cycle: int = -1) -> "ListNode":
        dummy = ListNode(-1)
        head = dummy
        mp = {}
        for i, _ in enumerate(data):
            head.next = cls(_)
            head = head.next
            mp[i] = head
        if cycle in mp:
            head.next = mp[cycle]
        return dummy.next

    def __str__(self):
        return f"val: {self.val}, next:{self.next and self.next.val or None}"

    __repr__ = __str__


def reverseLink(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return node


class Solution:
    def call(self, l1: List[int], l2: List[int]) -> List[int]:
        node = self.addTwoNumbers(ListNode.fromList(l1), ListNode.fromList(l2))
        if not node:
            return []
        return node.toList()

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        反转两个链表
        从最低位开始相加
        """
        l1 = reverseLink(l1)
        l2 = reverseLink(l2)
        dummy = ListNode(-1)
        node = dummy
        carry = 0
        while l1 or l2:
            cnt = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            node.next = ListNode(cnt % 10)
            node = node.next
            carry = int(cnt / 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            node.next = ListNode(carry)
        return reverseLink(dummy.next)


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[7, 2, 4, 3], [5, 6, 4]], "output": [7, 8, 0, 7]},
            {"input": [[2, 4, 3], [5, 6, 4]], "output": [8, 0, 7]},
            {"input": [[0], [0]], "output": [0]},
            {"input": [[1], [0]], "output": [1]},
            {"input": [[5], [5]], "output": [1, 0]},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
