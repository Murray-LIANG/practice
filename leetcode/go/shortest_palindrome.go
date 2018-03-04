package main

import (
	"fmt"
)

/*
https://leetcode.com/problems/shortest-palindrome

The solution is joining the original string S and the reversed string R.
For example, S = ACAD, R = DACA, join S and R, SR = ACAD#DACA.
ACAD#DACA
---   ---
The max prefix and suffix of SR is 3. So we just need to push D to the front of
S
Refer to kmp.go for calculating the max prefix and suffix.
 */

func reverse(b []byte, i int, j int) {
	for i < j {
		b[i], b[j] = b[j], b[i]
		i++
		j--
	}
}

func shortestPalindrome(s string) string {
	n, b, r := len(s), []byte(s), []byte(s)
	reverse(r, 0, n-1)
	newS := append(b, '#')
	newS = append(newS, r...)
	newN := 2*n + 1
	f := make([]int, newN)
	for i := 1; i < newN; i++ {
		t := f[i-1]
		for t > 0 && newS[i] != newS[t] {
			t = f[t-1]
		}
		if newS[i] == newS[t] {
			t++
		}
		f[i] = t
	}
	return string(append(r[:n-f[newN-1]], b...))
}

func main() {
	fmt.Println(shortestPalindrome("ACAD"))
}
