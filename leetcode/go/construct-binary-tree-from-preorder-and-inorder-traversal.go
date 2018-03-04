package main

import "fmt"

/*
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
 */

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {

	var helper func([]int, []int) *TreeNode
	helper = func(preorder []int, inorder []int) *TreeNode {
		if len(preorder) == 0 || len(inorder) == 0 {
			return nil
		}
		rootVal := preorder[0]
		root := &TreeNode{rootVal, nil, nil}
		rootInd := -1
		for index, v := range inorder {
			if v == rootVal {
				rootInd = index
				break
			}
		}
		root.Left = helper(preorder[1:rootInd+1], inorder[:rootInd])
		root.Right = helper(preorder[rootInd+1:], inorder[rootInd+1:])
		return root
	}
	return helper(preorder, inorder)
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
		if 2*index+1 <= count {
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
	root := buildTree([]int{1, 2, 4, 5, 7, 3, 6}, []int{4, 2, 7, 5, 1, 3, 6})
	fmt.Println(treeToSlice(root, 10))
}
