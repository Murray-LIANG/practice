package main

import (
	"sort"
	"fmt"
)

/*
https://leetcode.com/problems/combination-sum
 */

func combinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)

	res := [][]int{}
	var helper func(int, int, []int)
	helper = func(target int, start int, subres []int) {
		if target < 0 {
			return
		}
		if target == 0 {
			tmp := []int{}
			tmp = append(tmp, subres...)
			res = append(res, tmp)
		}

		for i:=start; i < len(candidates); i++{
			target -= candidates[i]
			subres = append(subres, candidates[i])
			helper(target, i, subres)
			subres = subres[:len(subres)-1]
			target += candidates[i]
		}
	}

	helper(target, 0, []int{})
	return res
}

func main() {
	fmt.Println(combinationSum([]int{2,3,6,7}, 7))
}
