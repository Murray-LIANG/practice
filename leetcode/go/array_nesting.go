package main

import "fmt"

// https://leetcode.com/problems/array-nesting/#/description

func arrayNesting(nums []int) int {
	count, step := 0, 0

	for i, _ := range nums {
		for nums[i] != -1 {
			k := nums[i]
			nums[i], i = -1, k
			step++
		}
		if step > count {
			count = step
		}
		step = 0
	}
	return count
}

func main() {
	fmt.Println(arrayNesting([]int{5,4,0,3,1,6,2}))
}
