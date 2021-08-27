#!/usr/bin/env python3
import unittest

"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = i = 0
        mp = {}
        for j, c in enumerate(s):
            if c in mp:
                # 由于mp[s[j]]指向的是上一个重复的字符
                # 所以需+1指向下一个不重复的字符
                i = max(i, mp[c] + 1)
            mp[c] = j
            count = max(count, j - i + 1)
        return count

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     start = data = 0
    #     indexs = {}
    #     for i in range(len(s)):
    #         x = s[i]
    #         if x in indexs:
    #             start = max(start, indexs[x] + 1)
    #         indexs[x] = i
    #         data = max(data, i - start + 1)
    #     return data


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {"input": ["abcabcbb"], "output": 3},
            {"input": ["bbbbb"], "output": 1},
            {"input": ["pwwkew"], "output": 3},
            {"input": [""], "output": 0},
            {"input": ["abcabcbb"], "output": 3},
            {"input": ["aabaab!bb"], "output": 3},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")

            self.assertEqual(
                Solution().lengthOfLongestSubstring(*t["input"]), t["output"]
            )


if __name__ == "__main__":
    unittest.main()
