package main

import (
	"fmt"
)

/**
 https://leetcode.com/problems/reverse-string-ii
 */
func reverseStr(s string, k int) string {
	b := []byte(s)
	n := len(b)
	for i := 0; i < n; i = i + 2*k {
		j := min(i+k-1, n-1)
		reverse(b, i, j)
	}
	return string(b)
}

func min(i int, j int) int {
	if i < j {
		return i
	}
	return j
}

func reverse(b []byte, i int, j int) {
	for i < j {
		b[i], b[j] = b[j], b[i]
		i++
		j--
	}
}

func main() {
	datas := []string{"abcdefg", "abcdef", "abcde", "abcd", "abc", "ab", "a"}
	for _, data :=range datas{
		fmt.Println("Test data:", data)
		fmt.Println("Reversed:", reverseStr(data, 2))
	}
}
