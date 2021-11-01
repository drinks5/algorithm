#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：

输入：s = "google"
输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
示例 2：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 3：

输入：s = "a"
输出：[["a"]]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return helper(s, len(s), 0, [], [])


def helper(
    s: str,
    length: int,
    start: int,
    substrings: List[str],
    ret: List[List[str]],
) -> List[List[str]]:
    if start == length:
        ret.append(list(substrings))
    elif start < length:
        for i in range(start, length):
            if isPalindrome(s, start, i):
                substrings.append(s[start: (i + 1)])
                ret = helper(s, length, i + 1, substrings, ret)
                substrings.pop()
    return ret


def isPalindrome(s: str, start: int, i: int) -> bool:
    while start < i:
        if s[start] != s[i]:
            return False
        start += 1
        i -= 1
    return True


cases = [
    {
        "input": ["google"],
        "output": [
            ["g", "o", "o", "g", "l", "e"],
            ["g", "oo", "g", "l", "e"],
            ["goog", "l", "e"],
        ],
    },
    {"input": ["aab"], "output": [["a", "a", "b"], ["aa", "b"]]},
    {"input": ["a"], "output": [["a"]]},
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().partition(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
