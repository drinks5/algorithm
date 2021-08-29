#!/usr/bin/env python
import unittest
from typing import List, Tuple
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


"""
给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

示例 1：

输入：head = [3,4,1], insertVal = 2
输出：[3,4,1,2]
解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。

示例 2：

输入：head = [], insertVal = 1
输出：[1]
解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。
示例 3：

输入：head = [1], insertVal = 0
输出：[1,0]
 
提示：

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6

链接：https://leetcode-cn.com/problems/4ueAj6
"""


# Definition for singly-linked list.
Node = ListNode


def reverseLink(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return node


class Solution:
    def call(self, data: List[int], val: int, cycle: int = -1) -> Tuple[int, int]:
        node = self.insert(ListNode.fromList(data, cycle), val)
        return node.val

    def insert(self, head: "Node", insertVal: int) -> "Node":
        node = Node(insertVal)
        if not head:
            head = node
            head.next = node
            return head
        if head.next == head:
            head.next = node
            head.next.next = head
            return head
        biggest = cur = head
        next = head.next
        while not (cur.val <= insertVal and next.val >= insertVal) and next != head:
            cur = next
            next = next.next
            if cur.val >= biggest.val:
                biggest = cur
        if cur.val <= node.val <= next.val:
            node.next = next
            cur.next = node
        else:
            node.next = biggest.next
            biggest.next = node
        return head


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[3, 3, 3], 0, 0], "output": 3},
            {"input": [[1, 3, 5], 1, 0], "output": 1},
            {"input": [[3, 4, 1], 2, 0], "output": 3},
            {"input": [[1, 3, 3], 4, 0], "output": 1},
            {"input": [[], 1], "output": 1},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
