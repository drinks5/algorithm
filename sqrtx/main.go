package main

func mySqrt(num int) int {
	var ans int
	low, high := 0, num
	mid := low + ((high - low) >> 1)
	for {
		ans = mid * mid
		if (high-low) <= 1 || ans == num {
			return mid
		}
		if ans > num {
			high = mid
		} else {
			low = mid
		}
	}
}
