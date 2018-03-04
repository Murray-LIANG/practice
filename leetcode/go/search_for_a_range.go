package main

import "fmt"

/*
https://leetcode.com/problems/search-for-a-range/#/description
We could use the same function to scan the list twice. This function could find
the first number whose value is equal to or greater than a target.
The first time we use `target` as the target, the second time we use `target+1`
as the target.
 */

func searchRange(nums []int, target int) []int {
	res, n := []int{-1, -1}, len(nums)
	if n == 0 {
		return res
	}
	lower1 := lowerBound(nums, target)
	if lower1 == -1 || nums[lower1] != target {
		return res
	}

	res[0] = lower1
	lower2 := lowerBound(nums, target+1)
	if lower2 == -1 {
		// maybe the last number is equal to the target
		res[1] = n - 1
	} else {
		res[1] = lower2 - 1
	}
	return res
}

func lowerBound(nums []int, target int) int {
	n := len(nums)
	i, j := 0, n-1
	for i < j {
		m := (i + j) / 2
		if nums[m] < target {
			i = m + 1
		} else {
			j = m
		}
	}
	if nums[i] < target {
		return -1
	} else {
		return i
	}
}

func main() {
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 8))
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 7))
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 10))
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 5))
	fmt.Println(searchRange([]int{}, 5))
	fmt.Println(searchRange([]int{1}, 0))
}
