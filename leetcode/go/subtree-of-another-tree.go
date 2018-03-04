package main

import "fmt"

/*
https://leetcode.com/problems/subtree-of-another-tree
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubtree(s *TreeNode, t *TreeNode) bool {

	var isSame func(*TreeNode, *TreeNode) bool
	isSame = func(t1 *TreeNode, t2 *TreeNode) bool {
		if t1 != nil && t2 != nil {
			return t1.Val == t2.Val && isSame(t1.Left, t2.Left) && isSame(t1.Right, t2.Right)
		} else {
			return t1 == t2
		}
	}

	if s == nil {
		return false
	}
	return isSame(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func main() {
	n1, n2, n3, n4, n5 :=
		&TreeNode{1, nil, nil},
		&TreeNode{2, nil, nil},
		&TreeNode{3, nil, nil},
		&TreeNode{4, nil, nil},
		&TreeNode{5, nil, nil}

	n3.Left, n3.Right = n4, n5
	n4.Left, n4.Right = n1, n2

	fmt.Println(isSubtree(n3, n4))

	n0, n1n, n2n, n4n := &TreeNode{0, nil, nil},
		&TreeNode{1, nil, nil},
		&TreeNode{2, nil, nil},
		&TreeNode{4, nil, nil}
	n4n.Left, n4n.Right = n1n, n2n
	n2n.Left = n0
	fmt.Println(isSubtree(n3, n4n))
}
