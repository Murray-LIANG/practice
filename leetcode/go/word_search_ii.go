package main

import "fmt"

func findWords(board [][]byte, words []string) []string {
	root := buildTrie(words)
	result := []string{}
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[row]); col++ {
			dfs(board, row, col, root, &result)
		}
	}
	return result
}

func dfs(board [][]byte, row int, col int, posInTrie *Trie, result *[]string) {
	c := board[row][col]
	if c == '#' {
		return
	}
	if _, ok := posInTrie.kids[rune(c)]; !ok {
		return
	}
	posInTrie = posInTrie.kids[rune(c)]
	if posInTrie.word != "" {
		*result = append(*result, posInTrie.word)
		posInTrie.word = ""  // avoid duplicate
	}
	board[row][col] = '#'
	if row > 0 {
		dfs(board, row - 1, col, posInTrie, result)
	}
	if row < len(board) - 1 {
		dfs(board, row + 1, col, posInTrie, result)
	}
	if col > 0 {
		dfs(board, row, col - 1, posInTrie, result)
	}
	if col < len(board[row]) - 1 {
		dfs(board, row, col + 1, posInTrie, result)
	}
	board[row][col] = c
}

type Trie struct {
	word string
	kids map[rune]*Trie
}

func NewTrie() *Trie {
	trie := new(Trie)
	trie.kids = map[rune]*Trie{}
	return trie
}

func buildTrie(words []string) *Trie {
	root := NewTrie()
	for _, word := range words {
		tmpNode := root
		for _, c := range word {
			if _, ok := tmpNode.kids[c]; !ok {
				tmpNode.kids[c] = NewTrie()
			}
			tmpNode = tmpNode.kids[c]
		}
		tmpNode.word = word
	}
	return root
}

func main() {
	board := [][]byte{
		{'o', 'a', 'a', 'n'},
		{'e', 't', 'a', 'e'},
		{'i', 'h', 'k', 'r'},
		{'i', 'f', 'l', 'v'},
	}
	words := []string{"oath", "pea", "eat", "rain"}
	fmt.Println(findWords(board, words))
}
