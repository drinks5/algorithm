#!/usr/bin/env python
from typing import Dict, Optional
import unittest

"""
运用所掌握的数据结构，设计和实现一个  LRU (Least Recently Used，最近最少使用) 缓存机制 。

实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 
提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
 
进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？

链接：https://leetcode-cn.com/problems/OrIXps
"""


class ListNode(object):
    def __init__(
        self,
        k: int,
        v: int,
        pre: Optional["ListNode"] = None,
        next: Optional["ListNode"] = None,
    ) -> None:
        self.key = k
        self.value = v
        self.pre = pre
        self.next = next

    def __str__(self):
        return f"key: {self.key}, value:{self.value}"

    __repr__ = __str__


class LRUCache:
    """
    哈希表+双向链表

    无法使用双向队列 deque，由于无法在O(1)的时间内把某个节点转移到queue的尾部
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp: Dict[int, ListNode] = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.move2Tail(node, node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            self.move2Tail(node, value)
            return
        if len(self.mp) == self.capacity:
            self.mp.pop(self.head.next.key)
            self.deleteNode(self.head.next)
        node = ListNode(key, value)
        self.insert2Tail(node)
        self.mp[key] = node

    def move2Tail(self, node: ListNode, value: int):
        self.deleteNode(node)
        node.value = value
        self.insert2Tail(node)

    def deleteNode(self, node: ListNode):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insert2Tail(self, node: ListNode):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class SolutionTestCase(unittest.TestCase):
    def test(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)
        lRUCache.put(3, 3)
        self.assertEqual(lRUCache.get(2), -1)
        lRUCache.put(4, 4)
        self.assertEqual(lRUCache.get(1), -1)
        self.assertEqual(lRUCache.get(3), 3)
        self.assertEqual(lRUCache.get(4), 4)


if __name__ == "__main__":
    unittest.main()
