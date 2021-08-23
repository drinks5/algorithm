package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if (p == nil && q != nil) || p != nil && q == nil || p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
func judge(left bool, right bool) {
	fmt.Printf("%s: %s\n", left, right)
}

func main() {
	judge(isSameTree(&TreeNode{Val: 1}, &TreeNode{Val: 2}), false)
	judge(isSameTree(&TreeNode{Val: 1}, &TreeNode{Val: 1}), true)
}
