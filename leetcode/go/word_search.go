package main

import "fmt"

func exist(board [][]byte, word string) bool {
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[row]); col++ {
			if dfs(board, word, row, col, 0) {
				return true
			}
		}
	}
	return false
}

func dfs(board [][]byte, word string, row int, col int, pos int) bool {
	if pos == len(word) {
		return true
	}
	if row < 0 || col < 0 || row == len(board) || col == len(board[row]) {
		return false
	}
	if board[row][col] != word[pos] {
		return false
	}
	tmp := board[row][col]
	board[row][col] = '#'
	// board[row][col] ^= 256
	result := (dfs(board, word, row - 1, col, pos + 1) ||
		dfs(board, word, row + 1, col, pos + 1) ||
		dfs(board, word, row, col - 1, pos + 1) ||
		dfs(board, word, row, col + 1, pos + 1))
	board[row][col] = tmp
	// board[row][col] ^= 256
	return result
}

type TestData struct {
	input string
	expected bool
}

func main() {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	datas := []TestData{{"ABCCED", true}, {"SEE", true}, {"ABCB", false}}
	for _, data := range datas {
		fmt.Println("Input word:", data.input)
		result := exist(board, data.input)
		fmt.Println("Output:", result)
		fmt.Println("Expected?", data.expected == result)
	}
}
