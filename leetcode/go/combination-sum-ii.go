package main

import (
	"sort"
	"fmt"
)

/*
https://leetcode.com/problems/combination-sum-ii
 */

func combinationSum2(candidates []int, target int) [][]int {
	res := [][]int{}
	sort.Ints(candidates)

	var helper func(int, int, []int)
	helper = func(target int, start int, subres []int) {
		if target < 0 {
			return
		}
		if target == 0 {
			res = append(res, append([]int{}, subres...))
		} else {
			for i:=start; i < len(candidates); i++ {
				if i != start && candidates[i] == candidates[i-1] {
					continue
				}
				target -= candidates[i]
				subres = append(subres, candidates[i])
				helper(target, i+1, subres)
				subres = subres[:len(subres) - 1]
				target += candidates[i]
			}
		}
	}
	helper(target, 0, []int{})
	return res
}

func main() {
	fmt.Println(combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8))
	fmt.Println(combinationSum2([]int{2,3,2,1,3,1}, 6))
}
