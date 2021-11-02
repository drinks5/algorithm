package restoreIpAddresses

import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	return helper(s, 0, []string{}, []string{})
}

func helper(s string, start int, substring []string, ret []string) []string {
	if start == len(s) && len(substring) == 4 {
		ret = append(ret, strings.Join(substring, "."))
	} else if start < len(s) {
		for i := start; i < len(s); i++ {
			if isValidSeg(s[start:i+1]) && len(substring) < 4 {
				substring = append(substring, s[start:i+1])
				ret = helper(s, i+1, substring, ret)
				substring = substring[:len(substring)-1]
			}
		}
	}
	return ret
}
func isValidSeg(seg string) bool {
	if i, err := strconv.ParseInt(seg, 10, 64); err != nil {
		return false
	} else {
		return 0 <= i && i < 256 && ((seg[0] != byte('0')) || seg == "0")

	}
}
