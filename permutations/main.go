package permutations

func permute(nums []int) [][]int {
	return helper(nums, len(nums), 0, [][]int{})
}

func helper(nums []int, length, i int, ret [][]int) [][]int {
	if i == length {
		dst := make([]int, length)
		copy(dst, nums)
		ret = append(ret, dst)
	} else if i < length {
		for j := i; j < length; j++ {
			nums[i], nums[j] = nums[j], nums[i]
			ret = helper(nums, length, i+1, ret)
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	return ret
}
