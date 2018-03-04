package main

import "fmt"

func nextGreaterElement(nums []int) []int {
	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		result[i] = -1
	}
	stack := []int{}  // put the index into the stack
	for i := 0; i < 2 * len(nums); i++ {
		num := nums[i % len(nums)]
		for len(stack) > 0 && nums[stack[len(stack) - 1]] < num {
			top := stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]
			result[top] = num
		}
		if i < len(nums) {
			stack = append(stack, i)
		}
	}
	return result
}

func main() {
	nums := []int{5, 2, 1, 4}
	fmt.Println(nextGreaterElement(nums))
}
