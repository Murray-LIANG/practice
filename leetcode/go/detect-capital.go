package main

import "fmt"

/*
https://leetcode.com/problems/detect-capital
 */

func detectCapitalUse(word string) bool {
	capitalCount := 0

	for _, ch := range word {
		if ch >= 'A' && ch <= 'Z' {
			capitalCount++
		}
	}
	return capitalCount == 0 ||
		capitalCount == len(word) ||
		(capitalCount == 1 && word[0] >= 'A' && word[0] <= 'Z')
}

func main() {
	fmt.Println(detectCapitalUse("USA"))
	fmt.Println(detectCapitalUse("China"))
	fmt.Println(detectCapitalUse("ChinA"))
}
