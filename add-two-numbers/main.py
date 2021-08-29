#!/usr/bin/env python3
import unittest
from typing import List
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from datastructures import ListNode


class Solution:
    def call(self, l1: List[int], l2: List[int]) -> List[int]:
        node = self.addTwoNumbers(ListNode.fromList(l1), ListNode.fromList(l2))
        if not node:
            return []
        return node.toList()

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l2:
            l2 = ListNode(0)
        if not l1:
            l1 = ListNode(0)
        l1.val = l1.val + l2.val
        if l1.val > 9:
            l1.val = l1.val - 10
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(1)
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[2, 4, 3], [5, 6, 4]], "output": [7, 0, 8]},
            {
                "input": [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]],
                "output": [8, 9, 9, 9, 0, 0, 0, 1],
            },
            {"input": [[0], [1]], "output": [1]},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().call(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
