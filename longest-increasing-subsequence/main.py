import typing


class Solution:
    def lengthOfLIS(self, nums: typing.List[int]) -> int:
        length = len(nums)
        dp = [1 for x in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


def main():
    inputs = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(inputs) == 4)


if __name__ == "__main__":
    main()
