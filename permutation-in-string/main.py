#!/usr/bin/env python3
import unittest
from typing import List

"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
             e i d b a o o 
            [-1,-1, 0, 1,1, 0,0
            [-1,-1,-1,0 ,0,-1,-1]
            [0,]
输出: False

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母

链接：https://leetcode-cn.com/problems/MPnaiL
"""


class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        length = len(t)
        if length > len(s):
            return False
        a = ord("a")
        counts = [0 for _ in range(26)]
        for i in range(length):
            counts[ord(t[i]) - a] += 1
            # 字符串 [0:length] 位为最开始指向的指针
            counts[ord(s[i]) - a] -= 1
        if all(x == 0 for x in counts):
            return True
        for i in range(length, len(s)):
            counts[ord(s[i]) - a] -= 1
            counts[ord(s[i - length]) - a] += 1
            if all(x == 0 for x in counts):
                return True
        return False
    # def checkInclusion(self, t: str, s: str) -> bool:
    #     """
    #     不能使用比特位
    #     比特位无法表示字符的次数， 如 aaa
    #     只能表示有无字符 a 
    #     """
    #     length = len(t)
    #     if length > len(s):
    #         return False
    #     a = ord("a")
    #     counts = 0
    #     for i in range(length):
    #         counts |= 1 << (ord(t[i]) - a)
    #         counts |= 1 >> (ord(s[i]) - a)
    #     print(counts)

    # def checkInclusion(self, t: str, s: str) -> bool:

    #     needs: dict[str, int] = {}
    #     windows: dict[str, int] = {}
    #     match = 0
    #     start = end = -1
    #     min_len = len(s) + 1
    #     i = j = 0
    #     for x in t:
    #         if x not in needs:
    #             needs[x] = 1
    #         else:
    #             needs[x] += 1
    #     for x in s:
    #         if x not in windows:
    #             windows[x] = 0

    #     while j < len(s):
    #         right = s[j]
    #         if right in needs:
    #             windows[right] += 1
    #             if windows[right] == needs[right]:
    #                 match += 1
    #         j += 1
    #         if match == len(needs):
    #             return True
    #     return False


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["ab", "eidbaooo"], "output": True},
            {"input": ["ab", "eidboaoo"], "output": False},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().checkInclusion(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
