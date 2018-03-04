package main

import "fmt"

/*
https://leetcode.com/problems/jump-game
 */

func canJump(nums []int) bool {
	n, maxJump := len(nums), 0

	for i := 0; i <= maxJump; i++ {
		if i+nums[i] > maxJump {
			maxJump = i + nums[i]
		}
		if maxJump >= n-1 {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
	fmt.Println(canJump([]int{3, 2, 1, 0, 4}))
	fmt.Println(canJump([]int{2, 5, 0, 0}))
	fmt.Println(canJump([]int{0}))
}
