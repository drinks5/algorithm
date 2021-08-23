#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import List


"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

链接：https://leetcode-cn.com/problems/1fGaJU
"""


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     暴力解法
    #     """
    #     length = len(nums)
    #     ans = set()
    #     for i in range(length):
    #         x = nums[i]
    #         for j in range(i + 1, length):
    #             y = nums[j]
    #             for k in range(j + 1, length):
    #                 z = nums[k]
    #                 if (x + y + z) == 0:
    #                     value = [x, y, z]
    #                     value.sort()
    #                     ans.add(tuple(value))
    #     return [list(x) for x in ans]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        思路：先计算两两之和存在字典里
        """
        length = len(nums)
        nums.sort()
        dp = defaultdict(set)
        index_map = {}
        ret = []
        for i in range(length - 1):
            x = nums[i]
            for j in range(i + 1, length):
                y = nums[j]
                tup = (x, y)
                if tup in index_map:
                    continue
                dp[x + y].add(tup)
                index_map[tup] = (i, j)
        for i in range(0, length):
            if nums[i] > 0:
                continue
            if (i + 1 < length) and nums[i] == nums[i + 1]:
                continue
            num = nums[i]
            for tup in dp[-num]:
                n, m = index_map[tup]
                if i != n and i != m:
                    ret.append([num, tup[0], tup[1]])
        return ret

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     三指针解法
    #     i < left < right
    #     i = 0
    #     left = i+1
    #     right = n-1
    #     """
    #     nums.sort()
    #     length, ret = len(nums), []
    #     for i in range(length - 2): # right = n-1, left = n-2, 所以i 最大遍历范围为 n-3
    #         if nums[i] > 0:  # 由于排过序，当第一个元素就大于0时，则直接跳过
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             # 由于left = i+1，所以当 i = n - 1时，left已经遍历过n了
    #             continue
    #         left = i + 1
    #         right = length - 1
    #         while left < right:
    #             ans = nums[i] + nums[left] + nums[right]
    #             if ans == 0:
    #                 ret.append([nums[i], nums[left], nums[right]])
    #                 val = nums[left]
    #                 while left < right and val == nums[left]:
    #                     left += 1
    #             elif ans < 0:
    #                 left += 1
    #             else:
    #                 right -= 1
    #     return ret


class SolutionTestCase(unittest.TestCase):
    def testthreeSum(self):
        table = [
            {"input": [[-1, 0, 1, 2, -1, -4]], "output": [[-1, -1, 2], [-1, 0, 1]]},
            {"input": [[]], "output": []},
            {"input": [[0]], "output": []},
            {"input": [[0, 0]], "output": []},
            {"input": [[-1, -2, 1, 2]], "output": []},
            {"input": [[0, 0, 0]], "output": [[0, 0, 0]]},
            {"input": [[1, 1, -2]], "output": [[-2, 1, 1]]},
        ]
        for t in table:
            self.assertListEqual(Solution().threeSum(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
