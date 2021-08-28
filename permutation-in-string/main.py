#!/usr/bin/env python3
from collections import defaultdict
from typing import Dict, List
import unittest

"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 
提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母

链接：https://leetcode-cn.com/problems/MPnaiL
"""


class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        length_t = len(t)
        length_s = len(s)
        if length_t > length_s:
            return False
        needs: dict[str, int] = defaultdict(int)
        windows: dict[str, int] = defaultdict(int)
        for i in range(length_t):
            windows[s[i]] += 1
            needs[t[i]] += 1
        if is_matched(windows, needs):
            return True
        for i in range(length_t, length_s):
            windows[s[i]] += 1
            windows[s[i - length_t]] -= 1
            if is_matched(windows, needs):
                return True
        return False


def is_matched(windows: Dict[str, int], needs: Dict[str, int]) -> bool:
    return all(needs[x] == windows[x] for x in needs)


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
