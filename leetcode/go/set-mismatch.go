package main

import (
	"fmt"
)

/*
https://leetcode.com/problems/set-mismatch
 */

func findErrorNums(nums []int) []int {
	res := []int{}

	var abs func(int) int
	abs = func(num int) int {
		if num < 0 {
			num = 0 - num
		}
		return num
	}

	for _, num := range nums {
		if nums[abs(num)-1] < 0 {
			res = append(res, abs(num))
		} else {
			nums[abs(num)-1] *= -1
		}
	}
	fmt.Println(nums)
	for index, num := range nums {
		if num > 0 {
			res = append(res, index+1)
			break
		}
	}
	return res
}

func main() {
	fmt.Println(findErrorNums([]int{3, 2, 1, 2}))
	fmt.Println(findErrorNums([]int{4, 2, 1, 2}))
}
