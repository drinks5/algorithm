package combinations

func combine(n int, k int) [][]int {
	if (n | k) == 0 {
		return [][]int{}
	}
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = i + 1

	}
	return helper(nums, 0, []int{}, [][]int{}, k)
}
func helper(nums []int, index int, subset []int, ret [][]int, k int) [][]int {
	if len(subset) == k {
		ret = append(ret, subset)
		return ret
	}
	if index == len(nums) {
		return ret
	}
	ret = helper(nums, index+1, subset, ret, k)
	subset = append(subset, nums[index])
	ret = helper(nums, index+1, subset, ret, k)
	return ret
}
