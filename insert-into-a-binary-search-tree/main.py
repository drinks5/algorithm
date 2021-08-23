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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        pass


def judge(left, right):
    print(f"{left}: {left == right}")


def main():
    judge(Solution().insertIntoBST, True)


if __name__ == "__main__":
    main()