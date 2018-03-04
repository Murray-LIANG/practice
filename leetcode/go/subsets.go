package main

import (
	"fmt"
	"sort"
	"container/list"
)

/*
https://leetcode.com/problems/subsets
 */

func subsets(nums []int) [][]int {
	res := [][]int{}
	tempRes := list.New()
	var dfs func(int)
	dfs = func(start int) {
		temp := []int{}
		for e := tempRes.Front(); e != nil; e = e.Next() {
			temp = append(temp, e.Value.(int))
		}
		res = append(res, temp)
		for i := start; i < len(nums); i++ {
			tempRes.PushBack(nums[i])
			dfs(i + 1)
			last := tempRes.Back()
			tempRes.Remove(last)
		}
	}
	sort.Ints(nums)
	dfs(0)
	return res
}

func main() {
	//fmt.Println(subsets([]int{1, 2, 3}))
	res := subsets([]int{9, 0, 3, 5, 7})
	fmt.Println(res)
}
