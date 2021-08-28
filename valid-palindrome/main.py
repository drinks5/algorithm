#!/usr/bin/env python
import unittest


"""
给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。

本题中，将空字符串定义为有效的 回文串 。

示例 1:

输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: s = "race a car"
输出: false
解释："raceacar" 不是回文串

提示：

1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成

链接：https://leetcode-cn.com/problems/XltzEq
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        count = 1
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["A man, a plan, a canal: Panama"], "output": True},
            {"input": ["race a car"], "output": False},
            {"input": [" "], "output": True},
            {"input": ["0P"], "output": False},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().isPalindrome(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
