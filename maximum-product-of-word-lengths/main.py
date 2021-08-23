#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import List


"""
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

示例 1:

输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
示例 2:

输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: words = ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
 

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/aseY1I
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解法
将字符串专为比特位
如abc转为 0000111
 efg专为 1110111
当两个字符串有重复的字符串时, x & y >0
否则 x & y = 0
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitByChar = {chr(ord("a") + i): i for i in range(26)}
        bitByWord = defaultdict(int)
        prd = 0
        for word in words:
            bit = 0
            for s in word:
                bit |= 1 << bitByChar[s]
            bitByWord[bit] = max(bitByWord[bit], len(word))
            for y in bitByWord:
                if (bit & y) == 0:
                    prd = max(bitByWord[y] * bitByWord[bit], prd)
        return prd


class SolutionTestCase(unittest.TestCase):
    def testAddBinary(self):
        table = [
            {"input": ["ab", "cd"], "output": 4},
            {"input": ["a", "ab", "abc", "d", "cd", "bcd", "abcd"], "output": 4},
            {"input": ["a", "aa", "aaa", "aaaa"], "output": 0},
            {"input": [], "output": 0},
        ]
        for t in table:
            self.assertEqual(Solution().maxProduct(t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
