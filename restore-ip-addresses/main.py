#!/usr/bin/env python
import unittest
from typing import List


"""
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址。
你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用
 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"和
"192.168@1.1" 是 无效 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "10203040"
输出：["10.20.30.40","102.0.30.40","10.203.0.40"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return helper(s, 0, [], [])


def helper(
    s: str, start: int, substring: List[str], ret: List[str]
) -> List[str]:
    if start == len(s) and len(substring) == 4:
        ret.append(".".join(substring))
    elif start < len(s):
        for end in range(start, len(s)):
            e = end + 1
            if isValidSeg(s[start:e]) and len(substring) < 4:
                substring.append(s[start:e])
                ret = helper(s, e, substring, ret)
                substring.pop()
    return ret


def isValidSeg(seg: str) -> bool:
    return 0 <= int(seg) < 256 and (seg[0] != "0" or seg == "0")


cases = [
    {"input": ["25525511135"], "output": ["255.255.11.135", "255.255.111.35"]},
    {"input": ["0000"], "output": ["0.0.0.0"]},
    {"input": ["1111"], "output": ["1.1.1.1"]},
    {"input": ["010010"], "output": ["0.10.0.10", "0.100.1.0"]},
    {
        "input": ["10203040"],
        "output": ["10.20.30.40", "10.203.0.40", "102.0.30.40"],
    },
]


class SolutionTestCase(unittest.TestCase):
    def test(self):
        for t in cases:
            print(f"input: {t['input']}\noutput: {t['output']}\n")
            ret = Solution().restoreIpAddresses(*t["input"])
            self.assertListEqual(ret, t["output"])


if __name__ == "__main__":
    unittest.main()
