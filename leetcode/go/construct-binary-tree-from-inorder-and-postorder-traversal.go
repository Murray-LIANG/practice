package main

import "fmt"

/*
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/
 */

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {

	var helper func([]int, []int) *TreeNode
	helper = func(inorder []int, postorder []int) *TreeNode {
		if len(inorder) == 0 || len(postorder) == 0 {
			return nil
		}
		rootVal := postorder[len(postorder)-1]
		root := &TreeNode{rootVal, nil, nil}
		rootInd := -1
		for index, v := range inorder {
			if v == rootVal {
				rootInd = index
				break
			}
		}
		root.Left = helper(inorder[:rootInd], postorder[:rootInd])
		root.Right = helper(inorder[rootInd+1:], postorder[rootInd:len(postorder)-1])
		return root
	}
	return helper(inorder, postorder)
}

func treeToSlice(root *TreeNode, count int) []int {
	queue := make([]*TreeNode, count+1)
	queue[1] = root
	for index := 1; index <= count/2; index++ {
		var left, right *TreeNode
		if queue[index] != nil {
			left = queue[index].Left
			right = queue[index].Right
		}
		queue[2*index] = left
		if 2 * index + 1 <= count {
			queue[2*index+1] = right
		}
	}
	res := []int{}
	for _, node := range queue {
		if node == nil {
			res = append(res, -1)
		} else {
			res = append(res, node.Val)
		}
	}
	return res
}

func main() {
	root := buildTree([]int{4, 2, 7, 5, 1, 3, 6}, []int{4, 7, 5, 2, 6, 3, 1})
	fmt.Println(treeToSlice(root, 10))
}
