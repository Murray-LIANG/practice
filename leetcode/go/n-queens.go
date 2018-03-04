package main

import "fmt"

/*
https://leetcode.com/problems/n-queens
 */

func solveNQueens(n int) [][]string {
	res := [][]string{}

	var isValid func([][]byte, int, int) bool
	isValid = func(nQueensPos [][]byte, row, col int) bool {
		for i:=0; i<row; i++ {
			if nQueensPos[i][col] == 'Q' {
				return false
			}
		}

		for i:=1; row-i>=0 && col-i>=0; i++ {
			if nQueensPos[row-i][col-i]=='Q' {
				return false
			}
		}

		for i:=1; row-i>=0 && col+i<n; i++ {
			if nQueensPos[row-i][col+i]=='Q' {
				return false
			}
		}
		return true
	}

	var helper func([][]byte, int)
	helper = func(nQueensPos [][]byte, row int) {
		if row == n {
			tmpRes := []string{}
			for _, pos := range nQueensPos {
				tmpRes = append(tmpRes, string(pos))
			}
			res = append(res, tmpRes)
			return
		}
		for col := 0; col < n; col++ {
			if isValid(nQueensPos, row, col) {
				nQueensPos[row][col] = 'Q'
				helper(nQueensPos, row+1)
				nQueensPos[row][col] = '.'
			}
		}
	}

	nQueensPos := [][]byte{}
	for i:=0 ; i<n; i++ {
		line := []byte{}
		for j:=0; j<n; j++ {
			line = append(line, '.')
		}
		nQueensPos = append(nQueensPos, line)
	}
	helper(nQueensPos, 0)
	return res
}

func main() {
	fmt.Println(solveNQueens(4))
}
