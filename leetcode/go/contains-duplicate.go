package main

import (
	"sort"
	"fmt"
)

/*
https://leetcode.com/problems/contains-duplicate
 */

func containsDuplicate(nums []int) bool {
	sort.Ints(nums)

	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{3, 4, 5, 2, 1, 3}))
}
