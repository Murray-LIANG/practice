package main

/*
https://leetcode.com/problems/binary-tree-preorder-traversal
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	res := []int{}

	stack := []*TreeNode{}
	current := root

	for len(stack) != 0 || current != nil {
		if current != nil {
			stack = append(stack, current)
			res = append(res, current.Val)
			current = current.Left
		} else {
			current = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			current = current.Right
		}
	}
	return res
}

func main() {
}
