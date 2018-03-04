package main

import "fmt"

/*
https://leetcode.com/problems/minesweeper

1. If M is clicked, mark X, and game over.
2. If E is clicked,
2.1 if any adjacent mine, mark the number of adjacent mine and stop.
2.2 if no adjacent mine, click all of its neighbors recursively.
 */

func updateBoard(board [][]byte, click []int) [][]byte {
	x, y := click[0], click[1]
	m, n := len(board), len(board[0])

	var validXY func(int, int) bool
	validXY = func(x int, y int) bool {
		return x >= 0 && x < m && y >= 0 && y < n
	}

	if board[x][y] == 'M' {
		board[x][y] = 'X'
	} else {
		adjacent := 0
		for i := -1; i < 2; i++ {
			for j := -1; j < 2; j++ {
				if i == 0 && j == 0 {
					continue
				}
				if validXY(x+i, y+j) && (board[x+i][y+j] == 'M' || board[x+i][y+j] == 'X') {
					adjacent++
				}
			}
		}
		if adjacent != 0 {
			board[x][y] = byte('0' + adjacent)
		} else {
			board[x][y] = 'B'
			for i := -1; i < 2; i++ {
				for j := -1; j < 2; j++ {
					if i == 0 && j == 0 {
						continue
					}
					if validXY(x+i, y+j) && board[x+i][y+j] == 'E' {
						updateBoard(board, []int{x + i, y + j})
					}
				}
			}
		}
	}
	return board
}

func main() {
	fmt.Println(updateBoard([][]byte{{'E', 'E', 'E', 'E', 'E'},
									 {'E', 'E', 'M', 'E', 'E'},
									 {'E', 'E', 'E', 'E', 'E'},
									 {'E', 'E', 'E', 'E', 'E'}},
		[]int{3, 0}))
}
