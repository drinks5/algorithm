#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import List


"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]
 

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 104

链接：https://leetcode-cn.com/problems/set-mismatch
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        ans = [0, 0]
        for x in nums:
            cnt[x] += 1
        for i in range(1, len(nums) + 1):
            count = cnt[i]
            if count == 0:
                ans[1] = i
            if count == 2:
                ans[0] = i

        return ans


class SolutionTestCase(unittest.TestCase):
    def testfindErrorNums(self):
        table = [
            {"input": [1, 2, 2, 4], "output": [2, 3]},
            {"input": [1, 1], "output": [1, 2]},
        ]
        for t in table:
            self.assertListEqual(
                Solution().findErrorNums(t["input"]), t["output"]
            )


if __name__ == "__main__":
    unittest.main()
