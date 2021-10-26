#!/usr/bin/env python
import unittest
from typing import List


"""
给定两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0 for x in range(1001)]
        for x in arr1:
            counts[x] += 1
        i = 0
        for x in arr2:
            while counts[x] > 0:
                arr1[i] = x
                counts[x] -= 1
                i += 1
        for num in range(1001):
            while counts[num] > 0:
                arr1[i] = num
                counts[num] -= 1
                i += 1
        return arr1


table = [
    {
        "input": [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]],
        "output": [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().relativeSortArray(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
