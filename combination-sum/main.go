package combinationSum

func combinationSum(candidates []int, target int) [][]int {
	return helper(candidates, 0, []int{}, [][]int{}, target)
}

func helper(nums []int, index int, subset []int, ret [][]int, target int) [][]int {
	if target == 0 {
		ret = append(ret, subset)
	} else if target > 0 && index < len(nums) {
		ret = helper(nums, index+1, subset, ret, target)
		subset = append(subset, nums[index])
		ret = helper(nums, index, subset, ret, target-nums[index])
	}
	return ret

}
