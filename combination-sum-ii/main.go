package combinationSum

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	return helper(candidates, 0, []int{}, [][]int{}, target)
}

func helper(nums []int, index int, subset []int, ret [][]int, target int) [][]int {
	if target == 0 {
		ret = append(ret, subset)
	} else if target > 0 && index < len(nums) {
		ret = helper(nums, getNext(nums, index), subset, ret, target)
		subset = append(subset, nums[index])
		ret = helper(nums, index+1, subset, ret, target-nums[index])
	}
	return ret
}

func getNext(nums []int, index int) int {
	next := index
	for {
		if next < len(nums) && nums[index] == nums[next] {
			next++
		} else {
			break
		}
	}
	return next
}
