package main

func singleNonDuplicate(nums []int) int {
	ret := 0
	for _, num := range nums {
		ret = ret ^ num
	}
	return ret
}
