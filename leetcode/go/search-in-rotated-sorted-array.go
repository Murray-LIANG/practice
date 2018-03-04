package main

import "fmt"

/*
https://leetcode.com/problems/search-in-rotated-sorted-array

Two solutions here:
1. Use binary search to find the rotation position. Then use binary search again
to search the target with the base is the rotation position.
2. Use binary search once. The mid element splits the array into two parts, one
is an ascending array, the other is the same as the original one with half of
elements. So no matter the target is in which side, the search is like the one
of original array but with size halved.
 */

func search(nums []int, target int) int {
	n := len(nums)
	if n == 0 {
		return -1
	}
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			return m
		}
		if nums[l] <= nums[m] { // `=` is for the last time compare.
			if nums[l] <= target && target < nums[m] {
				r = m - 1
			} else {
				l = m + 1
			}

		} else {
			if nums[m] < target && target <= nums[r] {
				l = m + 1
			} else {
				r = m - 1
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7}, 5))
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7}, 1))
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7}, 12))
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 6, 7}, 5))
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 6, 7}, 1))
	fmt.Println(search([]int{8, 9, 10, 11, 12, 1, 2, 3, 4, 6, 7}, 12))
	fmt.Println(search([]int{3, 1}, 1))
}
