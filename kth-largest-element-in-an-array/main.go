package main

func relativeSortArray(arr1 []int, arr2 []int) []int {
	counts := make([]int, 1001)
	for _, num := range arr1 {
		counts[num] += 1
	}
	i := 0
	for _, num := range arr2 {
		for {
			if counts[num] > 0 {
				arr1[i] = num
				counts[num] -= 1
				i++
			} else {
				break
			}
		}
	}
	for j, num := range counts {
		for {
			if num > 0 {
				arr1[i] = j
				num -= 1
				i++
			} else {
				break
			}
		}
	}
	return arr1
}
