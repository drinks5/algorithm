package subsets

func subsets(nums []int) [][]int {
	var ret [][]int
	if len(nums) == 0 {
		return ret
	}
	ret = helper(nums, 0, []int{}, ret)
	return ret
}

func helper(nums []int, index int, subset []int, result [][]int) [][]int {
	if len(nums) == index {
		return append(result, subset[:])
	}
	result = helper(nums, index+1, subset, result)
	subset = append(subset, nums[index])
	result = helper(nums, index+1, subset, result)
	return result
}
