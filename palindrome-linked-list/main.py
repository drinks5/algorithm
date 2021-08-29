#!/usr/bin/env python
import unittest
from typing import List
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


"""
给定一个链表的 头节点 head ，请判断其是否为回文链表。

如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。

示例 1：

输入: head = [1,2,3,3,2,1]
输出: true
示例 2：

输入: head = [1,2]
输出: fasle
 
提示：

链表 L 的长度范围为 [1, 105]
0 <= node.val <= 9

进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

链接：https://leetcode-cn.com/problems/aMhZSa
"""


# Definition for singly-linked list.
def reverseLink(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return node


class Solution:
    def call(self, data: List[int]) -> bool:
        return self.isPalindrome(ListNode.fromList(data))

    def isPalindrome(self, head: ListNode) -> bool:
        """
        寻找链表的中间节点，在中间节点处将链接分为两半，并将前半段反转
        如
        [1, 2, 3, 2, 1]
        分为
        [1, 2, 3]
        [5, 4]
        """
        dummy = ListNode(-1, head)
        slow = dummy
        fast = slow.next
        count = 0
        while fast:
            count += 1
            fast = fast.next
            slow = slow.next
            if fast:
                count += 1
                fast = fast.next
        second_half = slow.next
        if count % 2 == 0:
            slow.next = None
            return equals(reverseLink(head), second_half)
        slow.next = None
        return equals(reverseLink(head).next or head, second_half or head)


def equals(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 == l2


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 0, 1]], "output": True},
            {"input": [[1, 0, 0]], "output": False},
            {"input": [[1]], "output": True},
            {"input": [[1, 2]], "output": False},
            {"input": [[1, 2, 3, 3, 2, 1]], "output": True},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
