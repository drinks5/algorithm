#!/usr/bin/env python
import unittest
from typing import List


"""
狒狒喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

狒狒可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这
堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉，下一个小时才会开始吃另一堆的香蕉。  

狒狒喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while high > low:
            mid = low + ((high - low) >> 1)
            r = count(piles, mid)
            if r > h:
                low = mid + 1
            else:
                high = mid
        return low


def count(piles: List[int], mid: int) -> int:
    ret = 0
    for p in piles:
        ret += (p + mid - 1) // mid
    return ret


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[3, 6, 7, 11], 8], "output": 4},
            {"input": [[30, 11, 23, 4, 20], 5], "output": 30},
            {"input": [[30, 11, 23, 4, 20], 6], "output": 23},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().minEatingSpeed(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
