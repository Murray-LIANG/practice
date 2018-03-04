package main

import "fmt"

/*
https://leetcode.com/problems/longest-repeating-character-replacement

Forget the constraint K, let's take a look at the whole string S, if you want
to make minimal modification to make all the chars in S the same, you'll need
len(S) - count(most-frequent-char) steps of modification.

Take the constraint K into count, we could use a sliding window(size 0
initially). First expand the window and keep
len(window) - count(most-frequent-char) <= K, shrink the window from left
every time the size of window reach K+1.

Example:
 A A B C B B A, K=2
[A], len(window) = 1, count(most-frequent-char) = count(A) = 1
[A A], len(window) = 2, count(most-frequent-char) = count(A) = 2
[A A B], len(window) = 3, count(most-frequent-char) = count(A) = 2
[A A B C], len(window) = 4, count(most-frequent-char) = count(A) = 2
[A A B C B], len(window) = 5, count(most-frequent-char) = count(A) = 2, shrink!!!
[A B C B], len(window) = 4, count(most-frequent-char) = count(B) = 2
[A B C B B], len(window) = 5, count(most-frequent-char) = count(B) = 3
[A B C B B A], len(window) = 6, count(most-frequent-char) = count(B) = 3, shrink !!!
[B C B B A], len(window) = 5, count(most-frequent-char) = count(B) = 3
 */

func characterReplacement(s string, k int) int {
	left, right, maxWindowSize := 0, 0, 0
	count := make([]int, 26)
	maxCharCount := 0

	for ;right < len(s); right++{
		count[s[right]-'A']++
		if count[s[right]-'A'] >= maxCharCount {
			maxCharCount = count[s[right]-'A']
		}
		for right - left + 1 - maxCharCount > k {
			count[s[left]-'A']--
			left++
		}
		if right - left + 1 > maxWindowSize {
			maxWindowSize = right-left+1
		}
	}
	return maxWindowSize
}

func main() {
	fmt.Println(characterReplacement("AABCBBA", 2))
	fmt.Println(characterReplacement("AABCDBA", 2))
}
