package minCostClimbingStairs

func minCostClimbingStairs(cost []int) int {
	i := len(cost)
	dp := make([]int, i)
	return min(helper(cost, dp, i-1), helper(cost, dp, i-2))
}

func helper(cost []int, dp []int, i int) int {
	if i < 2 {
		dp[i] = cost[i]
		return cost[i]
	} else if dp[i] == 0 {
		dp[i] = min(helper(cost, dp, i-1), helper(cost, dp, i-2)) + cost[i]
	}
	return dp[i]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
