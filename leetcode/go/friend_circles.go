package main

import "fmt"


/*
https://leetcode.com/problems/friend-circles/#/description
Each person can be in one and only one circle. So use a map[int]bool to store
the info whether he has been visited.
For each person I, check the one (J) with whom he has relationship. And use
DFS to find all persons in the same circle. Recursively, for each J, if J
never visited, mark it visited, and just think dfs helper func could help find
all friends of J, like finding I's.
 */
func findCircleNum(M [][]int) int {
	count := 0
	n := len(M)
	visited := map[int]bool{}
	for i := 0; i < n; i++ {
		if ok, _ := visited[i]; !ok {
			dfs(M, i, visited)
			count++
		}
	}
	return count
}

func dfs(M [][]int, i int, visited map[int]bool) {
	n := len(M)
	for j := i; j < n; j++ {
		if ok, _ := visited[j]; !ok && M[i][j] == 1 {
			visited[j] = true
			dfs(M, j, visited)
		}
	}
}

func main() {
	M := [][]int{
		{1, 1, 0, 0, 1, 1},
		{1, 1, 0, 1, 0, 1},
		{0, 0, 1, 0, 0, 1},
		{0, 1, 0, 1, 0, 0},
		{1, 0, 0, 0, 1, 1},
		{1, 1, 1, 0, 1, 1},
	}
	fmt.Println(findCircleNum(M))
}
