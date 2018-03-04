package main

/*
https://leetcode.com/problems/binary-tree-level-order-traversal
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}
	if root == nil {
		return res
	}

	// All nodes in queue are in the same level.
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		subRes := []int{}
		for i:=0; i<levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			subRes = append(subRes, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, subRes)
	}
	return res
}

func main() {
}
