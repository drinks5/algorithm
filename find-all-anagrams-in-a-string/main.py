#!/usr/bin/env python3
from collections import defaultdict
import unittest
from typing import List, Dict

"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""


class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
        """
        滑动窗口
        windows记录窗口内的字符串数
        needs记录需要的字符串数
        使用单指针窗口大小固定为 len(t)
        """
        length_t = len(t)
        length_s = len(s)
        if length_t > length_s:
            return []
        needs: dict[str, int] = defaultdict(int)
        windows: dict[str, int] = defaultdict(int)
        matched: List[int] = []
        for i in range(length_t):
            windows[s[i]] += 1
            needs[t[i]] += 1
        if is_matched(windows, needs):
            matched.append(0)
        for i in range(length_t, length_s):
            windows[s[i]] += 1
            windows[s[i - length_t]] -= 1
            if is_matched(windows, needs):
                matched.append(i - length_t + 1)
        return matched


def is_matched(windows: Dict[str, int], needs: Dict[str, int]) -> bool:
    return all(needs[x] == windows[x] for x in needs)


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            # {"input": ["abab", "ab"], "output": [0, 1, 2]},
            # {"input": ["cbaebabacd", "abc"], "output": [0, 6]},
            {"input": ["af", "be"], "output": []},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().findAnagrams(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
