#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1

链接：https://leetcode-cn.com/problems/contiguous-array
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        无法用滑动窗口，因为非排序序列
        无法确定i,j的滑动方向
        相同数量的成对字符串，那么其和相加为0
        """
        length = len(nums)
        ret = 0
        mp = {0: -1}  # 当数组只有两个元素时， 1-(-1) = 2
        counter = 0
        for i in range(length):
            if nums[i] == 1:
                counter += 1
            else:
                counter -= 1
            if counter in mp:
                j = mp[counter]
                ret = max(i - j, ret)
            else:
                mp[counter] = i
        return ret


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            # {"input": [[0, 1]], "output": 2},
            # {"input": [[0, 1, 0]], "output": 2},
            {"input": [[0, 0, 1]], "output": 2},
            # {"input": [[]], "output": 0},
        ]
        for t in table:
            self.assertEqual(Solution().findMaxLength(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
