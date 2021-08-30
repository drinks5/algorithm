#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import Dict, List


"""
给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。

注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
示例 3:

输入: s = "a", t = "a"
输出: false
 
提示:

1 <= s.length, t.length <= 5 * 104
s and t 仅包含小写字母
 
进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

链接：https://leetcode-cn.com/problems/dKk3P7
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        counts: Dict[str, int] = defaultdict(int)
        for _ in s:
            counts[_] += 1
        for _ in t:
            counts[_] -= 1
            if counts[_] < 0:
                return False
        return True


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["anagram", "nagaram"], "output": True},
            {"input": ["rat", "car"], "output": False},
            {"input": ["a", "a"], "output": False},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().isAnagram(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
