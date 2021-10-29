package lengthOfLongestSubstring

func lengthOfLongestSubstring(s string) int {
	var count int
	var i int
	mp := make(map[rune]int)
	for j, c := range s {
		if val, ok := mp[c]; ok {
			if (val + 1) > i {
				i = val + 1
			}
		}
		mp[c] = j
		if (j - i + 1) > count {
			count = j - i + 1
		}
	}
	return count
}
