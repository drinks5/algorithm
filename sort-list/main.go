package main

import "math/rand"

func findKthLargest(arr []int, k int) int {
	pivot := arr[rand.Int()%(len(arr)-1)]
	var larger []int
	var equal []int
	var less []int
	for _, x := range arr {
		if x > arr[pivot] {
			larger = append(larger, x)
		} else if x == arr[pivot] {
			equal = append(equal, x)
		} else {
			less = append(less, x)
		}
	}
	if len(larger) >= k {
		return findKthLargest(larger, k)
	} else if len(larger)+len(equal) >= k {
		return arr[pivot]
	} else {
		return findKthLargest(append(equal, less...), k-len(larger))
	}
}
