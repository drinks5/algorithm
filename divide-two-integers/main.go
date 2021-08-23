package dividetwointegers

// func Add(a int, b int) int {
// 	if b == 0 {
// 		return a
// 	}
// 	return Add(a^b, (a&b)<<1)
// }
// func Negative(n int) int{
// 	return Add(~n, 1)
// }

// func DivideBit(a int, b int) int{
// 	if (0x80000000 == a) && (b == -1) {
// 		return 0x7FFFFFFF
// 	}
// 	return Add(a, negative(b))
// }
func Divide(a int, b int) int {
	if (0x80000000 == a) && (b == -1) {
		return 0x7FFFFFFF
	}
	negative := 2
	if a > 0 {
		negative -= 1
		a = -a
	}
	if b > 0 {
		negative -= 1
		b = -a
	}
	var ans int = 0
	for a <= b {
		ans += 1
		a -= b
	}
	if negative == 1 {
		return -ans
	}
	return ans
}
