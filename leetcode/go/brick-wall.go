package main

import "fmt"

/*
https://leetcode.com/problems/brick-wall
 */

func leastBricks(wall [][]int) int {
	height := len(wall)

	edge := map[int]int{}
	for _, layer := range wall {
		currentSum := 0
		for index, width := range layer {
			if index != len(layer)-1 {
				currentSum += width
				edge[currentSum]++
			}
		}
	}
	max := 0
	for _, v := range edge {
		if v > max {
			max = v
		}
	}
	return height - max
}

func main() {
	fmt.Println(leastBricks([][]int{{1, 2, 2, 1},
									{3, 1, 2},
									{1, 3, 2},
									{2, 4},
									{3, 1, 2},
									{1, 3, 1, 1}}))
}
