package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	var data *[]int
	traversal(root, data)
	return *data

}

func traversal(root *TreeNode, data *[]int) {
	if root == nil {
		return
	}
	*data = append(*data, root.Val)
	if root.Left != nil {
		traversal(root.Left, data)
	}
	if root.Right != nil {
		traversal(root.Right, data)
	}

}

func judge(left []int, right []int) {
	fmt.Printf("%s: %s\n", left, right)
}

func main() {
	judge(inorderTraversal(&TreeNode{Val: 1}), []int{1})
}
