#!/usr/bin/env python
import unittest
from typing import List
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

输入: head = [1,2,3,4]
输出: [1,4,2,3]
示例 2:

输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]

提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000
 
链接：https://leetcode-cn.com/problems/LGjMqU
"""


def reverseLink(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return node


class Solution:
    def call(self, data: List[int]) -> List[int]:
        head = ListNode.fromList(data)
        self.reorderList(head)
        return head.toList()

    def reorderList(self, head: ListNode) -> None:
        """
        寻找链表的中间节点，在中间节点处将链接分为两半, 然后穿插两个链表
        如
        [1, 2, 3, 4, 5]
        分为
        [1, 2, 3]
        [5, 4]

        [1, 2, 3, 4]
        分为
        [1, 2]
        [4, 3]
        """
        dummy = ListNode(-1, head)
        slow = dummy
        fast = dummy.next
        while fast:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
        right = slow.next
        slow.next = None
        left = dummy.next
        right = reverseLink(right)
        while left:
            node = left.next
            left.next = right
            if right:
                node2 = right.next
                right.next = node
                right = node2
            left = node

        return None


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 2, 3, 4]], "output": [1, 4, 2, 3]},
            {"input": [[1, 2, 3, 4, 5]], "output": [1, 5, 2, 4, 3]},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
