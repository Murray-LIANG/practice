package main

import (
	"fmt"
	"sort"
)

/*
https://leetcode.com/problems/permutations-ii/

The solution is similar with the one in permutations.

 */

func permuteUnique(nums []int) [][]int {
	sort.Sort(sort.IntSlice(nums))
	res := [][]int{}

	var recursion func([]bool, []int)
	recursion = func(visited []bool, subres []int) {
		// the index of visited is same as nums
		if len(subres) == len(nums) {
			tmp := []int{}
			tmp = append(tmp, subres...)
			res = append(res, tmp)
		}

		for index, num := range nums {
			if visited[index] {
				continue
			}
			if index != 0 && nums[index] == nums[index-1] && !visited[index-1] {
				continue
			}
			visited[index] = true
			subres = append(subres, num)
			recursion(visited, subres)
			subres = subres[:len(subres) -1]
			visited[index] = false
		}
	}
	visited := make([]bool, len(nums))
	recursion(visited, []int{})
	return res
}

func main() {
	//fmt.Println(permuteUnique([]int{1, 1, 1, 4, 5}))
	//fmt.Println(permuteUnique([]int{1, 2, 3, 4, 1}))
	//fmt.Println(permuteUnique([]int{1, 1, 2, 2}))
	//fmt.Println(permuteUnique([]int{1, 2, 2, 1}))
	//fmt.Println(permuteUnique([]int{0, 1, 0, 0, 9}))
	res := permuteUnique([]int{-1, -1, 0, 0, 1, 1, 2})

	fmt.Println("res: ", res)
	fmt.Println("len: ", len(res))
}
