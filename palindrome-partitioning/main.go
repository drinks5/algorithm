package palindromepartitioning

func partition(s string) [][]string {
	return helper(s, 0, []string{}, [][]string{})
}

func helper(s string, start int, substrings []string, ret [][]string) [][]string {
	if start == len(s) {
		ret = append(ret, substrings)
	} else {
		for i := start; i < len(s); i++ {
			if isPalindrome(s, start, i) {
				substrings = append(substrings, s[start:i+1])
				ret = helper(s, i+1, substrings, ret)
				substrings = substrings[:len(substrings)-1]
			}
		}
	}
	return ret
}

func isPalindrome(s string, i, j int) bool {
	for {
		if i < j {
			if s[i] != s[j] {
				return false
			}
			i++
			j--
		} else {
			return true
		}
	}
}
