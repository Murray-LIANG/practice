package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/word-ladder-ii

Use BFS.
 */

func findLadders(beginWord string, endWord string,
	wordList []string) [][]string {

	allWords := map[string]bool{}
	for _, word := range wordList {
		allWords[word] = true
	}
	var findNeighbors func(string) []string
	findNeighbors = func(word string) []string {
		res := []string{}
		chars := []byte(word)
		for index := range chars {
			for tmp := 'a'; tmp <= 'z'; tmp++ {
				if byte(tmp) == chars[index] {
					continue
				}
				archive := chars[index]
				chars[index] = byte(tmp)
				if _, ok := allWords[string(chars)]; ok {
					res = append(res, string(chars))
				}
				chars[index] = archive
			}
		}
		return res
	}

	neighbors := map[string][]string{}
	stepsFromBegin := map[string]int{beginWord: 0}

	queue := []string{beginWord}
	minSteps := math.MaxInt32
	for len(queue) != 0 {
		word := queue[0]
		queue = queue[1:]
		if stepsFromBegin[word] >= minSteps {
			continue
		}
		neighbors[word] = findNeighbors(word)
		for _, neighbor := range neighbors[word] {
			if _, ok := stepsFromBegin[neighbor]; !ok {
				stepsFromBegin[neighbor] = stepsFromBegin[word] + 1
				if neighbor != endWord {
					queue = append(queue, neighbor)
				} else if stepsFromBegin[neighbor] < minSteps {
					minSteps = stepsFromBegin[neighbor]
				}
			}
		}
	}

	res := [][]string{}
	var listPaths func(string, []string)
	listPaths = func(word string, path []string) {
		if len(path) > minSteps {
			return
		}
		if word == endWord {
			res = append(res, append(path, endWord))
		}
		for _, neighbor := range neighbors[word] {
			listPaths(neighbor, append(path, word))
		}
	}
	listPaths(beginWord, []string{})
	return res
}

func main() {
	fmt.Println(findLadders("hit", "cog",
		[]string{"hot", "dot", "dog", "lot", "log", "cog"}))
	fmt.Println(findLadders("red", "tax",
		[]string{"ted", "tex", "red", "tax", "tad", "den", "rex", "pee"}))
}
