#!/usr/bin/env python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        length = len(num1) + len(num2)
        result = [0 for x in range(length)]
        r1 = range(len(num1) - 1, -1, -1)
        r2 = list(range(len(num2) - 1, -1, -1))
        for i in r1:
            for j in r2:
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = result[p2] + mul
                result[p1] += total // 10
                result[p2] = total % 10
        i = 0
        for i in range(length):
            if result[i] != 0:
                break
        result = result[i:]
        return "".join(map(str, result))


def judge(left, right):
    print(f"{left}: {left == right}")


def main():
    judge(
        Solution().multiply("123", "456"),
        "56088",
    )
    judge(
        Solution().multiply("2", "3"),
        "6",
    )
    judge(
        Solution().multiply("2", "0"),
        "0",
    )


if __name__ == "__main__":
    main()