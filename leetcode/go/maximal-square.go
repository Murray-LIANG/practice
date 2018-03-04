package main

import "fmt"

/*
https://leetcode.com/problems/maximal-square

Use DP to solve this problem. We define the state to be the max size of the
square that can be achieved at point (i, j), denoted as S[i][j].

Then S[i][j] can be calculated from the value of S[i-1][j-1], S[i-1][j], and
S[i][j-1]. That is S[i][j] = min(S[i-1][j-1], S[i-1][j], S[i][j-1]) + 1. The
boundary is S[0][k] = matrix[0][k]. Only need to use one array to store the
info of S.
 */

func min(a int, b int) int {
	if a > b {
		return b
	}
	return a
}

func maximalSquare(matrix [][]byte) int {
	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	sizes := make([]int, n+1)
	maxSize := 0
	for i := 0; i < m; i++ {
		pre := sizes[0]
		for j := 0; j < n; j++ {
			tmp := sizes[j+1]
			if matrix[i][j] == '0' {
				sizes[j+1] = 0
			} else {
				sizes[j+1] = min(pre, min(sizes[j], sizes[j+1])) + 1
				if sizes[j+1] > maxSize {
					maxSize = sizes[j+1]
				}
			}
			pre = tmp
		}
	}
	return maxSize * maxSize
}

func main() {
	fmt.Println(maximalSquare([][]byte{[]byte("10100"),
									   []byte("10111"),
									   []byte("11111"), []byte("10010")}))
}
