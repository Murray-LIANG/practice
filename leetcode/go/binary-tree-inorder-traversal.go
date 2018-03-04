package main

/*
https://leetcode.com/problems/binary-tree-inorder-traversal
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {

	res := []int{}
	var helper func(*TreeNode)
	helper = func(node *TreeNode) {
		if node == nil {
			return
		}
		helper(node.Left)
		res = append(res, node.Val)
		helper(node.Right)
	}
	helper(root)
	return res
}

func inorderTraversalIterative(root *TreeNode) []int {
	res := []int{}

	stack := []*TreeNode{}
	current := root

	for len(stack) != 0 || current != nil {
		if current != nil {
			stack = append(stack, current)
			current = current.Left
		} else {
			current = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res = append(res, current.Val)
			current = current.Right
		}
	}
	return res
}



func main() {

}
