#!/usr/bin/env python3
import unittest

"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return ""


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["babad"], "output": "bab"},
            {"input": ["cbbd"], "output": "bb"},
            {"input": ["a"], "output": "a"},
            {"input": ["ac"], "output": "a"},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")

            self.assertEqual(
                Solution().longestPalindrome(*t["input"]), t["output"]
            )


if __name__ == "__main__":
    unittest.main()
