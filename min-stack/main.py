#!/usr/bin/env python
import unittest


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = -1 << 31
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self._min = x
            self.stack.append(x)
            return
        if x <= self._min:
            self.stack.append(self._min)
            self._min = x
            self.stack.append(x)
        else:
            self.stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] == self._min:
            self.stack.pop()
            self._min = self.stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def min(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


class SolutionTestCase(unittest.TestCase):
    def testMinStack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        minStack.push(0)
        minStack.min()
        minStack.pop()
        minStack.top()
        minStack.min()
        minStack.pop()


if __name__ == "__main__":
    unittest.main()
