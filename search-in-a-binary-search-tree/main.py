#!/usr/bin/env python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, data) -> "self":
        node = cls
        return cls()

    def to_list(self):
        pass


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def judge(left, right):
    print(f"{left}: {left == right}")


def main():
    judge(
        Solution().isSameTree(TreeNode.from_list(1, 2, 3), TreeNode.from_list(1, 2, 3)),
        True,
    )


if __name__ == "__main__":
    main()