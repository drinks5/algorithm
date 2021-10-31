#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return helper(nums, len(nums), 0, [])


def helper(
    nums: List[int],
    length: int,
    i: int,
    ret: List[List[int]],
) -> List[List[int]]:
    if length == i:
        ret.append(list(nums))
    elif i < length:
        for j in range(i, length):
            nums[i], nums[j] = nums[j], nums[i]
            ret = helper(nums, length, i + 1, ret)
            nums[i], nums[j] = nums[j], nums[i]
    return ret


cases = [
    {"input": [[1, 1, 2]], "output": [[1, 1, 2], [1, 2, 1], [2, 1, 1]]},
    {
        "input": [[1, 2, 3]],
        "output": [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().permuteUnique(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
