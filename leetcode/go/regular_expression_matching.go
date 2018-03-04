package main

import "fmt"

/*
 * https://leetcode.com/problems/regular-expression-matching
 * Use dp[i][j] to denote whether s[0..i] and p[0..j] matches or not.
 * dp[i][j] could be deduced from the value of dp[k][l] (k<=i, l<=j) based on
 * different cases:
 * case 1: if s[i] == p[j]: then dp[i][j] = d[i-1][j-1]
 * case 2: if p[j] == '.': because '.' matches any char, so dp[i][j] = d[i-1][j-1]
 * case 3: if p[j] == '*': there are several sub-cases:
 * 		3.1 if s[i] != p[j-1]:
 *				dp[i][j] = dp[i][j-2] (ie. aab ac*a*b, c* matches empty)
 *		3.2 if s[i] == p[j-1] or p[j-1] == '.':
 * 				dp[i][j] = any(
 *					dp[i-1][j] (ie. caab ca*b, a* matches multiple a, use p[j] (*) to match single a)
 *					dp[i][j-1] (ie. cab ca*b, a* matches single a, use p[j] (*) to match empty)
 *					dp[i][j-2] (ie. cb ca*b, a* matches empty)
 *
 * Boundary: the boundary is i = -1 and j = -1, which means
 * i points to the position before the first char in s, so empty string could
 * be matched by empty regex.
 *
 */

func isMatch(s string, p string) bool {
	m, n := len(s), len(p)
	if m == 0 || n == 0 {
		return false
	}

	dp := [][]bool{}
	for i := 0; i <= m; i++ {
		dp = append(dp, make([]bool, n+1))
	}
	dp[0][0] = true
	for i := 1; i <= n; i++ {
		if p[i-1] == '*' {
			dp[0][i] = dp[0][i-2]
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if s[i] == p[j] {
				dp[i+1][j+1] = dp[i][j]
			}
			if p[j] == '.' {
				dp[i+1][j+1] = dp[i][j]
			}
			if p[j] == '*' {
				if p[j-1] == s[i] || p[j-1] == '.' {
					dp[i+1][j+1] = dp[i][j+1] || dp[i+1][j] || dp[i+1][j-1]
				} else {
					dp[i+1][j+1] = dp[i+1][j-1]
				}
			}
			fmt.Println(dp)
		}
	}
	return dp[m][n]
}

func main() {
	fmt.Println(isMatch("aab", "c*a*b"))
}
