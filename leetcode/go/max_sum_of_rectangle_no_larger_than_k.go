package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k

We know how to solve the similar problem which is in 1D. Now this one is a 2D
version.
Based on the 1D solution, we add columns/rows line by line to combine the
rectangle(2D) to be in an array(1D).
For example, now we have a M*N matrix, and are on row I.
For each row J above row I (including I), sum up the value on the same
column from row I to row J. So we need a N-length array to store the sums
of value on the same column (in variable sumsCol). For each row J, like in 1D
solution, we traverse from 0 to N, store the current sum in variable `sum`,
for L between 0 and N, by calculating sum+matrix[J][L] we will get sum of the
rectangle of row (J..I) and column (0..L).
 */

func maxSumSubmatrix(matrix [][]int, k int) int {
	rows := len(matrix)
	if rows == 0 {
		return 0
	}
	cols := len(matrix[0])
	// if column num is greater than or equal to row num, we sum rows up.
	// otherwise, we sum columns up.
	moreColumns := cols > rows
	m, n := rows, cols
	if m > n {
		m, n = n, m
	}
	res := math.MinInt32
	for i := 0; i < m; i++ {
		sumsCol := make([]int, n)
		for j := i; j >= 0; j-- {
			// sumsRow is designed as:
			// sumsRow[0] = sum([])
			// sumsRow[1] = sum(nums[0])
			// sumsRow[2] = sum(nums[0..1])
			sumsRow := []int{0}
			sum := 0
			for l := 0; l < n; l++ {
				if moreColumns {
					sumsCol[l] += matrix[j][l]
				} else {
					sumsCol[l] += matrix[l][j]
				}
				sum += sumsCol[l]
				if s, ok := searchCeiling(sumsRow, sum-k); ok && sum-s > res {
					res = sum - s
				}
				sumsRow = append(sumsRow, sum)
			}
		}
	}
	return res
}

func searchCeiling(nums []int, num int) (int, bool) {
	res := math.MaxInt32
	for _, v := range nums {
		if v < num {
			continue
		}
		if v-num < res {
			res = v - num
		}
	}
	if res == math.MaxInt32 {
		return res, false
	} else {
		return res + num, true
	}
}

func main() {
	matrix := [][]int{
		{5, -4, -3, 4},
		{-3, -4, 4, 5},
		{5, 1, 5, -4},
	}
	fmt.Println(maxSumSubmatrix(matrix, 10))
}
