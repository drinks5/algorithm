#!/usr/bin/env python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        if self.val is None:
            return []
        data = [self.val]
        node = self.next
        while node:
            if node.val is not None:
                data.append(node.val)
            node = node.next
        return data

    @classmethod
    def from_list(self, *data):
        if not data:
            return ListNode()
        node = root = ListNode(data[0])
        for x in data[1:]:
            node.next = ListNode(x)
            node = node.next
        return root


class Solution:
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


def judge(left, right):
    print(left)
    print(left == right)


def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    data = Solution().addTwoNumbers(
        ListNode.from_list(2, 4, 3), ListNode.from_list(5, 6, 4)
    )
    judge(data.to_list(), [7, 0, 8])
    data = Solution().addTwoNumbers(
        ListNode.from_list(9, 9, 9, 9, 9, 9, 9), ListNode.from_list(9, 9, 9, 9)
    )
    judge(data.to_list(), [8, 9, 9, 9, 0, 0, 0, 1])
    data = Solution().addTwoNumbers(ListNode.from_list(0), ListNode.from_list(1))
    judge(data.to_list(), [1])
    data = Solution().addTwoNumbers(ListNode.from_list(0), ListNode.from_list(1))
    judge(data.to_list(), [1])
    data = Solution().addTwoNumbers(ListNode.from_list(0), ListNode.from_list(7, 3))
    judge(data.to_list(), [7, 3])


if __name__ == "__main__":
    main()