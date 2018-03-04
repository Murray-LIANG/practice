package main

import "fmt"

func strStr(haystack string, needle string) int {
	m := len(haystack)
	n := len(needle)
	for i := 0; i <= m - n; i++ {
		j := 0
		for ; j < n; j++ {
			if needle[j] != haystack[i + j] {
				break
			}
		}
		if j == n {
			return i
		}
	}
	return -1
}

func main() {
	haystack := "abcedfg"
	needle := "ced"
	fmt.Println(strStr(haystack, needle))
}

