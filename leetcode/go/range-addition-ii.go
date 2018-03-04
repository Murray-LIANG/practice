package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/range-addition-ii/
 */

func maxCount(m int, n int, ops [][]int) int {
	if len(ops) == 0 {
		return m * n
	}

	minA, minB := math.MaxInt32, math.MaxInt32
	for _, ab := range ops {
		if ab[0] < minA {
			minA = ab[0]
		}
		if ab[1] < minB {
			minB = ab[1]
		}
	}
	return minA * minB
}

func main() {
	fmt.Println(maxCount(3, 3, [][]int{{2, 2}, {3, 3}}))
}
