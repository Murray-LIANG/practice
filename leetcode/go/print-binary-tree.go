package main

import (
	"math"
	"fmt"
	"strconv"
)

/*
https://leetcode.com/problems/print-binary-tree
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func height(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftHeight, rightHeight := height(root.Left), height(root.Right)
	if leftHeight > rightHeight {
		return leftHeight + 1
	} else {
		return rightHeight + 1
	}
}

func printTree(root *TreeNode) [][]string {
	rows := height(root)
	cols := int(math.Pow(2, float64(rows)) - 1)
	res := make([][]string, rows)
	for i := range res {
		res[i] = make([]string, cols)
	}

	var helper func(node *TreeNode, layer int, start int, end int)
	helper = func(node *TreeNode, layer int, start int, end int) {
		if node == nil {
			return
		}
		index := (start + end) / 2
		res[layer][index] = strconv.Itoa(node.Val)
		helper(node.Left, layer+1, start, index-1)
		helper(node.Right, layer+1, index+1, end)
	}
	helper(root, 0, 0, cols-1)
	return res
}

func main() {
	n1, n2, n3, n4, n5 :=
		&TreeNode{1, nil, nil},
		&TreeNode{2, nil, nil},
		&TreeNode{3, nil, nil},
		&TreeNode{4, nil, nil},
		&TreeNode{5, nil, nil}
	n1.Left, n1.Right = n2, n5
	n2.Left = n3
	n3.Left = n4
	fmt.Println(printTree(n1))
}
