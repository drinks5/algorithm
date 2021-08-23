#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import List


"""
给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。

假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

 

示例 1：

输入：numbers = [1,2,4,6,10], target = 8
输出：[1,3]
解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[0,2]
示例 3：

输入：numbers = [-1,0], target = -1
输出：[0,1]
 

提示：

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kLl5u1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            ans = numbers[i] + numbers[j]
            if ans == target:
                return [i, j]
            if ans > target:
                j -= 1
            else:
                i += 1
        return []


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            {"input": [[1, 2, 4, 6, 10], 8], "output": [1, 3]},
            {"input": [[2, 3, 4], 6], "output": [0, 2]},
            {"input": [[-1, 0], -1], "output": [0, 1]},
        ]
        for t in table:
            self.assertEqual(Solution().twoSum(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
