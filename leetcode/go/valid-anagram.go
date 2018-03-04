package main

import "fmt"

/*
https://leetcode.com/problems/valid-anagram
 */

func isAnagram(s string, t string) bool {
	seen := map[byte]int{}
	for _, b := range s {
		seen[byte(b)]++
	}
	for _, b := range t {
		seen[byte(b)]--
	}
	for _, v := range seen {
		if v != 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(isAnagram("a", "aa"))
	fmt.Println(isAnagram("aaa", "aa"))
}
