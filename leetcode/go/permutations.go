package main

import "fmt"

/*
https://leetcode.com/problems/permutations
 */

func permute(nums []int) [][]int {
	res := [][]int{}

	var recursion func([]int, []int)
	recursion = func(unvisited []int, visited []int) {
		if len(unvisited) == 0 {
			res = append(res, visited)
		}

		for index, num := range unvisited {
			visited = append(visited, num)
			unvisited = append(unvisited[:index], unvisited[index+1:]...)
			recursion(unvisited, visited)
			tmp := append([]int{}, num)
			tmp = append(tmp, unvisited[index:]...)
			unvisited = append(unvisited[:index], tmp...)
			visited = visited[:len(visited)-1]
		}
	}
	recursion(nums, []int{})
	return res
}

func permute2(nums []int) [][]int {
	res := [][]int{}

	var recursion func(int)
	recursion = func(index int) {
		// nums[:index] are visited, nums[index:] are un-visited.
		if index == len(nums) {
			tmp :=[]int{}
			tmp = append(tmp, nums...)
			res = append(res, tmp)
		}

		for i := index; i < len(nums); i++{
			nums[index], nums[i] = nums[i], nums[index]
			recursion(index+1)
			nums[index], nums[i] = nums[i], nums[index]
		}
	}
	recursion(0)
	return res
}

func main() {
	fmt.Println(permute([]int{1, 2, 3, 4, 5}))
	fmt.Println(permute2([]int{1, 2, 3, 4, 5}))
	fmt.Println(permute([]int{1, 2, 3}))
	fmt.Println(permute2([]int{1, 2, 3}))
}
