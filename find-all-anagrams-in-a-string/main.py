#!/usr/bin/env python3
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
from typing import List


class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:

        needs: dict[str, int] = {}
        windows: dict[str, int] = {}
        match = 0
        matched: List[int] = []
        i = j = 0
        nums = len(t)
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
                if j - i == nums:
                    matched.append(i)
                if left in needs:
                    windows[left] -= 1
                    if windows[left] < needs[left]:
                        match -= 1
                i += 1
        return matched


def judge(left, right):
    print(left)
    print(left == right)


def main():
    # judge(Solution().findAnagrams("abab", "ab"), [0, 1, 2])
    # judge(Solution().findAnagrams("cbaebabacd", "abc"), [0, 6])
    # judge(Solution().findAnagrams("baa", "aa"), [1])
    judge(Solution().findAnagrams("abacbabc", "abc"), [1, 2, 3, 5])


if __name__ == "__main__":
    main()