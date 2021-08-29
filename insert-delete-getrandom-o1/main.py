#!/usr/bin/env python
import random
import unittest


"""
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构：

insert(val)：当元素 val 不存在时返回 true ，并向集合中插入该项，否则返回 false 。
remove(val)：当元素 val 存在时返回 true ，并从集合中移除该项，否则返回 false 。
getRandom：随机返回现有集合中的一项。每个元素应该有 相同的概率 被返回。
 
示例 :

输入: inputs = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出: [null, true, false, true, 2, true, false, 2]
解释:
RandomizedSet randomSet = new RandomizedSet();  // 初始化一个空的集合
randomSet.insert(1); // 向集合中插入 1 ， 返回 true 表示 1 被成功地插入

randomSet.remove(2); // 返回 false，表示集合中不存在 2 

randomSet.insert(2); // 向集合中插入 2 返回 true ，集合现在包含 [1,2] 

randomSet.getRandom(); // getRandom 应随机返回 1 或 2 
  
randomSet.remove(1); // 从集合中移除 1 返回 true 。集合现在包含 [2] 

randomSet.insert(2); // 2 已在集合中，所以返回 false 

randomSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 
 
提示：

-231 <= val <= 231 - 1
最多进行 2 * 105 次 insert ， remove 和 getRandom 方法调用
当调用 getRandom 方法时，集合中至少有一个元素

链接：https://leetcode-cn.com/problems/FortPu
"""


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indexByNum = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indexByNum:
            return False
        self.indexByNum[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.indexByNum:
            return False
        index = self.indexByNum[val]
        lastVal = self.nums[-1]
        self.nums[index] = lastVal
        self.indexByNum[lastVal] = index
        self.indexByNum.pop(val)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        randomSet = RandomizedSet()
        self.assertEqual(randomSet.insert(1), True)
        self.assertEqual(randomSet.remove(2), False)
        self.assertEqual(randomSet.insert(2), True)
        randomSet.getRandom()
        self.assertEqual(randomSet.remove(1), True)
        self.assertEqual(randomSet.insert(2), False)
        self.assertEqual(randomSet.getRandom(), 2)

        randomSet = RandomizedSet()
        self.assertEqual(randomSet.insert(0), True)
        self.assertEqual(randomSet.insert(1), True)
        self.assertEqual(randomSet.remove(0), True)
        self.assertEqual(randomSet.insert(2), True)
        self.assertEqual(randomSet.remove(1), True)
        self.assertEqual(randomSet.getRandom(), 2)

if __name__ == "__main__":
    unittest.main()
