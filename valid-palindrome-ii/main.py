#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

示例 1:

输入: s = "aba"
输出: true
示例 2:

输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符
示例 3:

输入: s = "abc"
输出: false

提示:

1 <= s.length <= 105
s 由小写英文字母组成

链接：https://leetcode-cn.com/problems/RQku0D
"""


def judge(s, i, j, count):
    while i < j:
        if s[i] != s[j]:
            if count:
                return judge(s, i + 1, j, count-1) or judge(s, i, j - 1, count-1)
            return False
        else:
            i += 1
            j -= 1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 1
        i, j = 0, len(s) - 1
        return judge(s, i, j, count)

    # def validPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     count = 1
    #     i, j = 0, len(s) - 1
    #     while i <= j:
    #         if not s[i].isalnum():
    #             i += 1
    #         elif not s[j].isalnum():
    #             j -= 1
    #         else:
    #             if s[i] != s[j]:
    #                 if count:
    #                     if (i + 1 <= j) and (s[i + 1] == s[j]):
    #                         i += 1
    #                         count -= 1
    #                         continue
    #                     elif (j - 1 >= i) and (s[i] == s[j - 1]):
    #                         j -= 1
    #                         count -= 1
    #                         continue
    #                 return False
    #             i += 1
    #             j -= 1
    #     return True


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            {"input": ["abxfa"], "output": True},
            # {"input": [" "], "output": True},
            # {"input": ["abca"], "output": True},
            # {"input": ["acba"], "output": True},
            # {"input": ["abc"], "output": False},
            # {"input": ["eeccccbebaeeabebccceea"], "output": False},
            # {
            #     "input": [
            #         "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
            #     ],
            #     "output": True,
            # },
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().validPalindrome(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
