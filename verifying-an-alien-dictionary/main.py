#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import Dict, List


"""
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

示例 1：

输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
示例 2：

输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
示例 3：

输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。

链接：https://leetcode-cn.com/problems/lwyVBB
"""

a = ord("a")


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        counts = [0 for i in range(26)]
        for i, _ in enumerate(order):
            counts[ord(_) - a] = i
        for i in range(len(words) - 1):
            if not isSorted(words[i], words[i + 1], counts):
                return False
        return True


def isSorted(word1: str, word2: str, counts: List[str]) -> bool:
    length = min(len(word1), len(word2))
    i = 0
    while i < length:
        if counts[ord(word1[i]) - a] > counts[ord(word2[i]) - a]:
            return False
        if counts[ord(word1[i]) - a] < counts[ord(word2[i]) - a]:
            return True
        i += 1
    return i == len(word1)


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {
                "input": [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"],
                "output": True,
            },
            {
                "input": [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"],
                "output": False,
            },
            {
                "input": [["apple", "app"], "abcdefghijklmnopqrstuvwxyz"],
                "output": False,
            },
            {
                "input": [["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"],
                "output": True,
            },
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertEqual(Solution().isAlienSorted(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
