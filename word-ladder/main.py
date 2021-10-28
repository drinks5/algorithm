#!/usr/bin/env python
import unittest
from typing import List, Tuple


"""
https://leetcode.com/problems/word-ladder/
在字典（单词列表） wordList 中，从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给定两个长度相同但内容不同的单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord
 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。

示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
"log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
"log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
"""

Dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

"""
    hit dot dog
hit     1
dot   1
dog
"""

class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        length = len(beginWord)
        wordsLength = len(wordList)
        if not beginWord:
            return 0
        graph = [[-1] * length for _ in range(length)]
        wordList.insert(0, beginWord)
        for i in range(wordsLength):
            for j in range(i, wordsLength):
                match = 0
                for k in range(length):
                    if wordList[i][k] == wordList[j][k]:
                        match += 1
                if match == (length - 1):
                    graph[i][j] = j
                    graph[j][i] = i
        stack = [0]
        while stack:
            v = stack.pop()
            for n in graph[v]:
                
            

        return 0


cases = [
    {
        "input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
        "output": 5,
    },
    {
        "input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
        "output": 0,
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().ladderLength(*t["input"])
            self.assertEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
