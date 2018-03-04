package main

import "fmt"

/*
https://leetcode.com/problems/contains-duplicate-ii
 */

func containsNearbyDuplicate(nums []int, k int) bool {
	visited := map[int]bool{}
	for j := 0; j <= k && j < len(nums); j++ {
		if visited[nums[j]] {
			return true
		}
		visited[nums[j]] = true
	}

	for i := 1; i < len(nums); i++ {
		visited[nums[i-1]] = false
		if i+k < len(nums) {
			if visited[nums[i+k]] {
				return true
			}
			visited[nums[i+k]] = true
		}
	}
	return false
}

func main() {
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 4, 5}, 1))
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 4, 5}, 2))
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 4, 5}, 3))
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 6, 4, 1}, 5))

}
