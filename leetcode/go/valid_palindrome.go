package main

import (
	"strings"
	"fmt"
)

func isalnum(b byte) bool {
	return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
}

func isPalindrome(s string) bool {
	i, j := 0, len(s) - 1
	s = strings.ToLower(s)
	for i < j {
		for i < j && !isalnum(s[i]) {
			i++
		}
		for i < j && !isalnum(s[j]) {
			j--
		}
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func main() {
	datas := [][]string{
		{"A man, a plan, a canal: Panama", "true"},
		{"race a car", "false"},
		{"0P", "false"},
		{"", "true"},
	}

	for index, data := range datas {
		fmt.Println("Test round #", index)
		fmt.Println("Test data:", data[0])
		result := isPalindrome(data[0])
		fmt.Println("Expected: ", result)
	}
}
