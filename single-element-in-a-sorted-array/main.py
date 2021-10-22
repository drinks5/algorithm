#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个只包含整数的有序数组 nums ，每个元素都会出现两次，唯有一个数只会出现一次，请找出这个唯一的数字。

示例 1:

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: nums =  [3,3,7,7,10,11,11]
输出: 10

提示:

1 <= nums.length <= 105
0 <= nums[i] <= 105
 
进阶: 采用的方案可以在 O(log n) 时间复杂度和 O(1) 空间复杂度中运行吗？
"""


class Solution:
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     ret = 0
    #     for num in nums:
    #         ret ^= num
    #     return ret
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = int(low + ((high - low) >> 1))
            mid = mid if mid % 2 == 0 else (mid - 1)
            if nums[mid] == nums[mid + 1]:
                low = low + 2
            else:
                high = mid
        return nums[low]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": [[1, 1, 2, 3, 3, 4, 4, 8, 8]], "output": 2},
            {"input": [[3, 3, 7, 7, 10, 11, 11]], "output": 10},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().singleNonDuplicate(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
