#!/usr/bin/env python3
from collections import defaultdict
import unittest

"""
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。

如果 s 中存在多个符合条件的子字符串，返回任意一个。

注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC" 
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3：

输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
 
提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 
进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

链接：https://leetcode-cn.com/problems/M1oyTv
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        使用滑动窗口
        windows 记录 窗口内每个元素出现的次数
        needs 记录窗口内需要每个元素出现的次数
        当在窗口内时，windows的每个元素应该大于needs的每个元素
        """
        needs = defaultdict(int)
        windows = defaultdict(int)
        ret = (0, 0)
        length = len(s) + 1
        i = 0
        for _ in t:
            needs[_] += 1
        for j, x in enumerate(s):
            windows[x] += 1
            while is_matched(windows, needs) and i <= j:
                windows[s[i]] -= 1
                if (j - i + 1) < length:
                    ret = (i, j + 1)
                    length = j - i + 1
                i += 1
        return s[ret[0] : ret[1]]


def is_matched(windows, needs):
    return all(windows[_] >= needs[_] for _ in needs)


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["a", "a"], "output": "a"},
            {"input": ["ADOBECODEBANC", "ABC"], "output": "BANC"},
            {"input": ["a", "aa"], "output": ""},
            {"input": ["", ""], "output": ""},
            {"input": ["a", ""], "output": ""},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().minWindow(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
