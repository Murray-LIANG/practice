package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/perfect-squares
 */

func numSquares(n int) int {
	// Top down solution, timeout.
	start := int(math.Sqrt(float64(n)))
	if start == 1 {
		return n
	}
	if n == start*start {
		return 1
	}
	min := math.MaxInt32
	for i := start; i >= 1; i-- {
		tmp := 1 + numSquares(n-i*i)
		if tmp < min {
			min = tmp
		}
	}

	return min
}

func numSquares2(n int) int {
	// Bottom up solution with memo.

	var min func(int, int) int
	min = func(a, b int) int {
		if a > b {
			return b
		}
		return a
	}

	memo := make([]int, n+1)
	for index := range memo {
		memo[index] = math.MaxInt32
	}
	memo[0] = 0

	for i := 1; i <= n; i++ {
		for j := 1; j*j <= i; j++ {
			memo[i] = min(memo[i], memo[i-j*j]+1)
		}
	}
	return memo[n]
}

func main() {
	fmt.Println(numSquares2(16))
	fmt.Println(numSquares2(12))
	fmt.Println(numSquares2(4))
	fmt.Println(numSquares2(62))
}
