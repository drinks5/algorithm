#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

提示：

1 <= target <= 109
1 <= nums.length <=j 105
1 <= nums[i] <= 105
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
 
链接：https://leetcode-cn.com/problems/2VG8Kg
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        前缀和+暴力解法
        前缀和+二分查找
        """
        length = len(nums)
        pre = [0 for x in range(length + 1)]
        ret = len(nums) + 1
        for i in range(1, length + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        for n in range(length):
            x = target + pre[n - 1]
            index = binary_search(pre, 0, length - 1, x)
            if index < 0:
                index = ~index
            if index <= length:
                ret = min(ret, index - n)
        return 0 if ret == (len(nums) + 1) else ret

    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     """
    #     滑动窗口
    #     """
    #     length = len(nums)
    #     ret = len(nums) + 1
    #     i = j = 0
    #     ans = 0
    #     while j < length:
    #         ans += nums[j]
    #         while ans >= target:
    #             ret = min(j - i + 1, ret)
    #             ans -= nums[i]
    #             i += 1
    #         j += 1
    #     return 0 if ret == (len(nums) + 1) else ret


class SolutionTestCase(unittest.TestCase):
    def testminSubArrayLen(self):
        table = [
            {"input": [1, [1]], "output": 1},
            {"input": [15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]], "output": 2},
            {"input": [15, [1, 2, 3, 4, 5]], "output": 5},
            {"input": [11, [1, 2, 3, 4, 5]], "output": 3},
            {"input": [7, [2, 3, 1, 2, 4, 3]], "output": 2},
            {"input": [4, [1, 4, 4]], "output": 1},
            {"input": [11, [1, 1, 1, 1, 1, 1, 1, 1]], "output": 0},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().minSubArrayLen(*t["input"]), t["output"])


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -(high + low) // 2


if __name__ == "__main__":
    print(binary_search([2, 5, 7, 10, 15, 18, 20], 0, 6, 9))
    unittest.main()
