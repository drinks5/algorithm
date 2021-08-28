#!/usr/bin/env python
import unittest
from typing import List


"""
给你一个整数数组 nums ，请计算数组的 中心下标 。
数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

示例 1：

输入：nums = [1,7,3,6,5,6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
示例 2：

输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
示例 3：

输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
 

提示：

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
链接：https://leetcode-cn.com/problems/tvdfij
"""


class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    #     if not nums:
    #         return -1
    #     length = len(nums)
    #     pre = [0 for _ in range(length + 1)]
    #     for i in range(1, length + 1):
    #         pre[i] = pre[i - 1] + nums[i - 1]
    #     if (pre[-1] - pre[1]) == 0:
    #         return 0
    #     for i in range(length):
    #         #  [2,-2,5,2,-2]
    #         # [0,2,0,5,7,5]

    #         #  [-2,5,-2]
    #         # [0,-2,3,1]


    #         #  [5, -1, 1]
    #         # [0,5, 4, 5]
    #         if pre[i] == (pre[-1] - pre[i + 1]):
    #             return i
    #     return -1
    def pivotIndex(self, nums: List[int]) -> int:
        """
         [1,2,3,2,1]
        前缀和
        [0,1,3,6,8,9]
        sum[-1] = 9
        sum[3] - a[3] = 9 - sum[3] = 3
        """
        total = sum(nums)
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if (count - nums[i]) == (total - count):
                return i
        return -1


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 7, 3, 6, 5, 6]], "output": 3},
            {"input": [[1, 2, 3]], "output": -1},
            {"input": [[2, 1, -1]], "output": 0},
            {"input": [[-1, 1, 5]], "output": 2},
            {"input": [[-1, -1, -1, 1, 1, 1]], "output": -1},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().pivotIndex(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
