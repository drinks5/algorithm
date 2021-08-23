#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0
 
提示: 

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
 

注意：本题与主站 713 题相同：https://leetcode-cn.com/problems/subarray-product-less-than-k/ 

链接：https://leetcode-cn.com/problems/ZVAVXX
"""


class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     """
    #     滑动窗口
    #     """
    #     if k == 0:
    #         return 0
    #     total = 1
    #     i = count = 0
    #     for j in range(len(nums)):
    #         total *= nums[j]
    #         while (i <= j) and (total >= k):
    #             total /= nums[i]
    #             i += 1
    #         if i <= j:  # 元素本身也符合 <k 的条件
    #             count += j - i + 1
    #     return count
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        前缀积
        """
        if k == 0:
            return 0
        length = len(nums)
        pre = [1 for _ in range(len(nums) + 1)]
        count = 0
        for i in range(length):
            pre[i + 1] = pre[i] * nums[i]
        for j in range(1, length + 1):
            for i in range(1, j + 1):
                if pre[j] / pre[i] < k:
                    count += j - i + 1
                    break
        return count


class SolutionTestCase(unittest.TestCase):
    def testminSubArrayLen(self):
        table = [
            {"input": [[10, 5, 2, 6], 100], "output": 8},
            {"input": [[1, 2, 3], 0], "output": 0},
            {"input": [[], 1], "output": 0},
            {"input": [[1, 2, 3], 6], "output": 4},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(
                Solution().numSubarrayProductLessThanK(*t["input"]), t["output"]
            )


if __name__ == "__main__":
    unittest.main()
