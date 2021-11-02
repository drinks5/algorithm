package houserobberii

func rob(nums []int) int {
	a := 0
	if len(nums) < 3 {
		for i := 0; i < len(nums); i++ {
			a = max(a, nums[i])
		}
		return a
	}
	return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
}

func helper(nums []int) int {
	if len(nums) < 3 {
		return max(nums[0], nums[1])
	}
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	dp[1] = nums[1]
	dp[2] = nums[2] + nums[0]
	for i := 3; i < len(nums); i++ {
		dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
	}
	return max(dp[len(nums)-1], dp[len(nums)-2])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
