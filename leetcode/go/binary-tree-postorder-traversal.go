package main

/*
https://leetcode.com/problems/binary-tree-postorder-traversal
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	// like the one in preorder traversal, but the `res` stores the value in
	// reverse order of final answer.
	res := []int{}

	stack := []*TreeNode{}
	current := root

	for len(stack) != 0 || current != nil {
		if current != nil {
			stack = append(stack, current)
			res = append(res, current.Val)
			current = current.Right
		} else {
			current = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			current = current.Left
		}
	}

	var reverse func([]int)
	reverse = func(res []int) {
		for i, j := 0, len(res)-1; i < j; i++ {
			res[i], res[j] = res[j], res[i]
			j--
		}
	}
	reverse(res)
	return res
}

func main() {
}
