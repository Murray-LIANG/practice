package main

import (
	"strings"
	"fmt"
	"strconv"
)

/*
 * https://leetcode.com/problems/binary-tree-paths
 *
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func helper(root *TreeNode, currentPath []string, allPaths []string) []string {
	currentPath = append(currentPath, strconv.Itoa(root.Val))
	if root.Left == nil && root.Right == nil {
		allPaths = append(allPaths, strings.Join(currentPath, "->"))
	}
	if root.Left != nil {
		allPaths = helper(root.Left, currentPath, allPaths)
	}
	if root.Right != nil {
		allPaths = helper(root.Right, currentPath, allPaths)
	}
	return allPaths
}

func binaryTreePaths(root *TreeNode) []string {
	allPaths := []string{}
	if root != nil {
		allPaths = helper(root, []string{}, []string{})
	}
	return allPaths
}

func binaryTreePaths_2(root *TreeNode) []string {
	if root == nil {
		return nil
	}
	paths := []string{}
	var traverse func(*TreeNode, []string)
	traverse = func(node *TreeNode, current []string) {
		current = append(current, strconv.Itoa(node.Val))
		if node.Left == nil && node.Right == nil {
			paths = append(paths, strings.Join(current, "->"))
		}
		if node.Left != nil {
			traverse(node.Left, current)
		}
		if node.Right != nil {
			traverse(node.Right, current)
		}
	}
	traverse(root, []string{})
	return paths
}

func main() {
	n5 := TreeNode{5, nil, nil}
	n3 := TreeNode{3, nil, nil}
	n2 := TreeNode{2, nil, &n5}
	n1 := TreeNode{1, &n2, &n3}
	fmt.Println(binaryTreePaths_2(&n1))
}
