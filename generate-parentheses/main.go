package generateParenthesis

func generateParenthesis(n int) []string {
	return helper(n, n, "", []string{})
}

func helper(left, right int, parentThesis string, ret []string) []string {
	if (left | right) == 0 {
		ret = append(ret, parentThesis)
		return ret
	}
	if left > 0 {
		ret = helper(left-1, right, parentThesis+"(", ret)
	}
	if left < right {
		ret = helper(left, right-1, parentThesis+")", ret)
	}
	return ret
}
