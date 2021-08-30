#!/usr/bin/env python
from collections import defaultdict
import unittest
from typing import Dict, List


"""
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。

注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母

链接：https://leetcode-cn.com/problems/sfvd7V
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[str, List[str]] = defaultdict(list)
        for _ in strs:
            key = ",".join(sorted(_))
            groups[key].append(_)
        return list(groups.values())


class SolutionTestCase(unittest.TestCase):
    def test(self):
        table = [
            {
                "input": [["eat", "tea", "tan", "ate", "nat", "bat"]],
                "output": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            },
            {"input": [[""]], "output": [[""]]},
            {"input": [["a"]], "output": [["a"]]},
        ]
        for t in table:
            print(f"input: {t['input']}\noutput: {t['output']}")
            self.assertListEqual(Solution().groupAnagrams(*t["input"]), t["output"])


if __name__ == "__main__":
    unittest.main()
