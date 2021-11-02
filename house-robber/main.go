package houserobber

func rob(nums []int) int {
	n := len(nums)
	if n < 3 {
		if n == 1 {
			return nums[0]
		}
		return max(nums[0], nums[1])
	}
	dp := make([]int, n)
	dp[0] = nums[0]
	dp[1] = nums[1]
	dp[2] = nums[0] + nums[2]
	for i := 3; i < n; i++ {
		dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

	}
	return max(dp[n-2], dp[n-1])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
