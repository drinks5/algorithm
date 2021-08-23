#!/usr/bin/env python3
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


from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = data = 0
        indexs = {}
        for i in range(len(s)):
            x = s[i]
            if x in indexs:
                start = max(start, indexs[x] + 1)
            indexs[x] = i
            data = max(data, i - start + 1)
        return data


def judge(left, right):
    print(f"{left}: {left == right}")


def main():
    judge(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
    judge(Solution().lengthOfLongestSubstring("bbbbb"), 1)
    judge(Solution().lengthOfLongestSubstring("pwwkew"), 3)
    judge(Solution().lengthOfLongestSubstring(""), 0)
    judge(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
    judge(Solution().lengthOfLongestSubstring("aabaab!bb"), 3)


if __name__ == "__main__":
    main()
