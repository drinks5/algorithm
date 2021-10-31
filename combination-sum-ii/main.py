#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return helper(nums, 0, [], [])


def helper(
    nums: List[int],
    i: int,
    subset: List[int],
    ret: List[List[int]],
) -> List[List[int]]:
    if i == len(nums):
    elif i < len(nums) and target > 0:
        ret = helper(nums, getNext(nums, i), target, subset, ret)
        subset.append(nums[i])
        ret = helper(nums, i + 1, target - nums[i], subset, ret)
        subset.pop()
    return ret


def getNext(nums: List[int], i: int) -> int:
    cur = i
    while cur < len(nums) and nums[cur] == nums[i]:
        cur += 1
    return cur


cases = [
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
    {"input": [[0, 1]], "output": [[0, 1], [1, 0]]},
    {"input": [[1]], "output": [[1]]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().permute(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
