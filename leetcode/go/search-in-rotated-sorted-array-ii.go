package main

import "fmt"

/*
https://leetcode.com/problems/search-in-rotated-sorted-array-ii
 */

func search(nums []int, target int) bool {
	n := len(nums)
	if n == 0 {
		return false
	}
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			return true
		}
		if nums[l] == nums[m] {
			l++
		} else if nums[l] < nums[m] {
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
	return false
}

func main() {
	fmt.Println(search([]int{1, 3, 1, 1, 1}, 3))
}
