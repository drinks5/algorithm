package main

func minEatingSpeed(piles []int, h int) int {
	var (
		high int = 1
		low  int = 1
		mid  int = 0
		r    int = 0
	)
	for _, x := range piles {
		if x > high {
			high = x
		}
	}
	for {
		if high == low {
			break
		}
		mid = low + ((high - low) >> 1)
		r = count(piles, mid)
		if r > h {
			low = mid + 1
		} else {
			high = mid
		}
	}
	return low
}

func count(piles []int, mid int) int {
	ret := 0
	for _, p := range piles {
		ret = ret + (p+mid-1)/mid
	}
	return ret
}
