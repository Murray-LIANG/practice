package main

import "fmt"

/*
https://leetcode.com/problems/search-insert-position
 */

func searchInsert(nums []int, target int) int {
	n := len(nums)
	i, j := 0, n-1
	for i <= j {
		m := (i + j) / 2
		if nums[m] == target {
			return m
		}
		if nums[m] < target {
			i = m + 1
		} else {
			j = m - 1
		}
	}
	return i
}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 7))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 0))
	fmt.Println(searchInsert([]int{1, 3, 5, 6, 8}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6, 8}, 2))
	fmt.Println(searchInsert([]int{1, 3, 5, 6, 8}, 7))
	fmt.Println(searchInsert([]int{1, 3, 5, 6, 8}, 9))
	fmt.Println(searchInsert([]int{1, 3, 5, 6, 8}, 0))
}
