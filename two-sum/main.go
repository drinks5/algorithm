package main

func twoSum(nums []int, target int) []int {
	counts := make(map[int]int)
	for i, n := range nums {
		diff := target - n
		if val, ok := counts[diff]; ok {
			return []int{val, i}
		} else {
			counts[n] = i
		}

	}
	return []int{}
}
