package painthouse

func minCost(costs [][]int) int {
	x := 0
	for i := 1; i < 3; i++ {
		if costs[0][i] > costs[0][x] {
			x = i
		}
	}
	dp := make([][]int, len(costs))
	for i, _ := range dp {
		dp[i] = make([]int, 3)
	}
	return min(helper(costs, dp, 0, (x+1)%3), helper(costs, dp, 0, (x+2)%3))
}

func helper(costs [][]int, dp [][]int, i, j int) int {
	if i == len(costs) {
		return 0
	}
	if dp[i][j] != 0 {
		return dp[i][j]
	}
	dp[i][j] = min(helper(costs, dp, i+1, (j+1)%3), helper(costs, dp, i+1, (j+2)%3)) + costs[i][j]
	return dp[i][j]

}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
