package main

import (
	"strings"
	"fmt"
)

/*
https://leetcode.com/problems/remove-duplicate-letters

For string S, from left to right, find the new string NewS which
1. starts from the index `minStart` in S,
2. the chars on the left side of minStart will appear after minStart.
3. S[minStart] is the smallest char in S[minStart...].

 */

func removeDuplicateLetters(s string) string {
	if len(s) == 0 {
		return ""
	}
	count := map[int32]int{}
	for _, ch := range s{
		count[ch] += 1
	}
	minStart := 0
	for index, ch := range s {
		if byte(ch) < byte(s[minStart]) {
			minStart = index
		}
		count[ch] -= 1
		if count[ch] == 0 {
			break
		}
	}
	newS := strings.Replace(s[minStart+1:], string(s[minStart]), "", -1)
	return string(s[minStart]) + removeDuplicateLetters(newS)
}

func main() {
	fmt.Println(removeDuplicateLetters("cbacdcbc"))
}
