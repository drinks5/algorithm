#!/usr/bin/env python3
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
        needs: dict[str, int] = {}
        windows: dict[str, int] = {}
        match = 0
        start = end = -1
        min_len = len(s) + 1
        i = j = 0
        for x in t:
            if x not in needs:
                needs[x] = 1
            else:
                needs[x] += 1
        for x in s:
            if x not in windows:
                windows[x] = 0

        while j < len(s):
            right = s[j]
            if right in needs:
                windows[right] += 1
                if windows[right] == needs[right]:
                    match += 1
            j += 1
            while match == len(needs):
                left = s[i]
                if (j - i) < min_len:
                    min_len = j - i
                    start = i
                    end = j
                if left in needs:
                    windows[left] -= 1
                    if windows[left] < needs[left]:
                        match -= 1
                i += 1

        return s[start:end]


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
