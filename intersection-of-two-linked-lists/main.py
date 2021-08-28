#!/usr/bin/env python
import unittest
from typing import Dict, List, Optional


"""
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

进阶：能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？

链接：https://leetcode-cn.com/problems/3u1WK4
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

    def length(self) -> int:
        return getLinkLength(self)

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


def getLinkLength(node: ListNode) -> int:
    head = ListNode(-1, node)
    count = 0
    while head.next:
        count += 1
        head = head.next
    return count


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
    def call(self, a: List[int], b: List[int]) -> int:
        node = self.getIntersectionNode(ListNode.fromList(a), ListNode.fromList(b))
        return node.val

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        遍历两个链表得到长度l1,l2
        在长的链表上先走 abs(l1-l2) 步
        如p1,p2指针
        p2
        |
        9-8-7
            - 5-4
        1-2-3-10
         |
         p1
        """
        lengthA = getLinkLength(headA)
        lengthB = getLinkLength(headB)
        if (lengthA - lengthB) > 0:
            shorter = headB
            longer = headA
        else:
            shorter = headA
            longer = headB
        for i in range(abs(lengthA - lengthB)):
            longer = longer.next
        while longer and shorter:
            if longer == shorter:
                return shorter
            shorter = shorter.next
            longer = longer.next
        return None

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     """
    #     使用双栈记录两个链表
    #     链表重合的部分在栈顶
    #     """
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     """
    #     思路
    #     9-8-7
    #         - 5-4
    #     1-2-3
    #     把重合链表改为环形链表
    #     9-8-7-5-4--1
    #         | |
    #         3--2
    #     从而题目转化为求环形链表的入环点
    #     """
    #     pass


class SolutionTestCase(unittest.TestCase):
    def test(self):
        pass
        # table = [
        #     {"input": [[4,1,8,4,5], ], "output": 2},
        #     {"input": [[1], -1], "output": -1},
        #     {"input": [[1, 2], 0], "output": 1},
        # ]
        # for t in table:
        #     print(f"input: {t['input']}\noutput: {t['output']}")
        #     self.assertEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
