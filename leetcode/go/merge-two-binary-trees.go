package main

/*
https://leetcode.com/problems/merge-two-binary-trees

 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil && t2 == nil {
		return nil
	}

	res := &TreeNode{0, nil, nil}
	var t1Left, t1Right, t2Left, t2Right *TreeNode
	if t1 != nil {
		res.Val += t1.Val
		t1Left, t1Right = t1.Left, t1.Right
	}
	if t2 != nil {
		res.Val += t2.Val
		t2Left, t2Right = t2.Left, t2.Right
	}
	res.Left = mergeTrees(t1Left, t2Left)
	res.Right = mergeTrees(t1Right, t2Right)
	return res
}

func main() {
}
