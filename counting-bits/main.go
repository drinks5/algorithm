package addbinary

/*
偶数n的位数与n/2的位数一致，因为 n >> 1 = n/2
奇数的位数与n/2+1一致
*/

func countBits(n int) []int {
	var i int
	ans := make([]int, n+1)
	for i = 0; i < n+1; i++ {

		ans[i] = ans[i>>1] + (i & 1)
	}
	return ans
}
