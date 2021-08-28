#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 
提示：

1 <= s.length <= 1000
s 由小写英文字母组成

链接：https://leetcode-cn.com/problems/a7VOhD
"""


def counting(s: str, length, i: int, j: int) -> int:
    count = 0
    while (0 <= i) and (j < length) and (s[i] == s[j]):
        i -= 1
        count += 1
        j += 1
    return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        如果回文长度是奇数，那么回文中心是一个字符
        如果回文长度是偶数，那么中心是两个字符
        """
        count = 0
        i, length = 0, len(s)
        for i in range(0, len(s)):
            count += counting(s, length, i, i)
            count += counting(s, length, i, i + 1)
        return count


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            # {"input": ["abc"], "output": 3},
            {"input": ["aaa"], "output": 6},
            {"input": [" "], "output": 1},
            {"input": [""], "output": 0},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().countSubstrings(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
