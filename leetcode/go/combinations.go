package main

import "fmt"

/*
https://leetcode.com/problems/combinations
 */

func combine(n int, k int) [][]int {
	if k > n {
		return [][]int{}
	}

	var helper func(int, int) [][]int
	helper = func(n int, k int) [][]int {
		if k == 0 {
			return [][]int{{}}
		}

		res := [][]int{}
		for i := n; i > 0; i-- {
			tmp := helper(i-1, k-1)
			for _, item := range tmp {
				res = append(res, append(item, i))
			}
		}
		return res
	}
	return helper(n, k)
}

func main() {
	fmt.Println(combine(4, 2))
}
