#!/usr/bin/env python3
from typing import List
import unittest


"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        前缀和
        """

        counter = ret = 0
        mp = {0: 1}
        for i in range(len(nums)):
            counter += nums[i]
            ret += mp.get(counter - k, 0)
            mp[counter] = mp.get(counter, 0) + 1
        return ret

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """
    #     滑动窗口
    #     由于数组可能有负数，无法使用滑动窗口
    #     """
    #     ans = count = i = 0
    #     for j in range(len(nums)):
    #         ans += nums[j]
    #         while i <= j:
    #             if ans == k:
    #                 count += 1
    #             if ans > k:
    #                 ans -= nums[i]
    #             i += 1
    #     return count


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            # {"input": [[1, 1, 1], 2], "output": 2},
            # {"input": [[1, 2, 3], 3], "output": 2},
            # {"input": [[], 3], "output": 0},
            # {"input": [[1, 2, 3], 6], "output": 1},
            {"input": [[1, -1, 0], 0], "output": 3},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().subarraySum(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
