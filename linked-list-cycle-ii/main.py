#!/usr/bin/env python
import unittest
from typing import Dict, List, Optional


"""
给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 
提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引

进阶：是否可以使用 O(1) 空间解决此题？

链接：https://leetcode-cn.com/problems/c32eOV
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
        return f"val: {self.val}"

    __repr__ = __str__


def getNodeInLoop(head: ListNode) -> Optional[ListNode]:
    if not head or not head.next:
        return None
    slow = head.next
    fast = slow.next
    while slow and fast:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return None


class Solution:
    def call(self, data: List[int], cycle: int) -> int:
        node = self.detectCycle(ListNode.fromList(data, cycle))
        if not node:
            return -1
        return node.val

    def detectCycle(self, head: ListNode) -> ListNode:
        in_loop = getNodeInLoop(head)
        if not in_loop:
            return None
        current = head
        count = 0
        while current != in_loop:
            count += 1
            current = current.next
        fast = head
        slow = head
        for _ in range(count):
            fast = fast.next
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[3, 2, 0, -4], 1], "output": 2},
            {"input": [[1], -1], "output": -1},
            {"input": [[1, 2], 0], "output": 1},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
