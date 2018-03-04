package main

import "fmt"

/*
Given a string S, and a pattern string P, find the position in S where P matches.
For example,
S = CDABCDABCDB
P = CDABCDB

** Solution I: Brute-force **
The brute force solution is: index I points to chars in S, index J points to P.
Check S[I] and P[J], if they matches, I++, J++. If not, I = I - J + 1, J = 0.
That is, shift P one char left from current matching beginning.
    C   I
S oooooox
P   ooooX
        J
C is the current matching beginning, I, J point to char of S and P.
So C = I - J.
Next round,
     I
S oooooox
P    ooooX
     J

** Solution II: KMP **
The key point of KMP is remember the max length of prefix and suffix, marked as
F, which is useful when shifting the P string. This time P doesn't shifted one
by one char. Instead, it shifts the count of chars based on the value of F.
		  I
S = CDABCDABCDB
P = CDABCDB
		  J
F = 0000120
Say we are checking S[I] (A) and P[J] (B), which doesn't match. Then we let
J = F[J-1] = 2, and keep I not changed.
		  I
S = CDABCDABCDB
P =     CDABCDB
		  J
Which means that shift P 4 chars left. It is more efficient than the brute-force
solution.
Now the problem is how to build the F values.
Index	0123456789abcdef
P		CDABCDAECDABCDAB
		------- -------
F   	        1234567I
OCP, we are calculating the F value of P[I], and we know the values before I,
like F[I-1] = 7, so we need to check P[I] == P[F[I-1]] or not, if yes, the
matched prefix and suffix extends, that is F[I] = F[I-1] + 1. If no, we need to
check the shorter prefix.
Index	0123456789abcdef
P		CDABCDAECDABCDAB
		--- ---
F   	0000123        I
That is, check P[I] == P[F[F[I-1]-1]] or not,
where P[F[F[I-1]-1]] = P[F[7-1]] = P[F[6]] = P[3]. If P[I] == P[3], the matched
prefix and suffix would be same as the F[6] = 3. That is P[I] extends the length
of prefix and suffix of P[0123456], because P[cdeI] == P[456I] == p[0123]. So
now we have a recursive way to calculate F values.
 */

func kmp(S string, P string) int {
	m, n := len(S), len(P)
	f := make([]int, n)
	for i := 1; i < n; i++ {
		t := f[i-1]
		for t > 0 && P[i] != P[t] {
			t = f[t-1]
		}
		if P[i] == P[t] {
			t++
		}
		f[i] = t
	}
	i, j := 0, 0
	for i < m && j < n {
		if S[i] == P[j] {
			i++
			j++
		} else if j == 0 || j == f[j-1] {
			i++
			j = 0
		} else if j != 0 {
			j = f[j-1]
		}
	}
	if j == n {
		return i - j
	}
	return -1
}

func main() {
	fmt.Println(kmp("CDABCDABCDC", "CDABCDB"))
	fmt.Println(kmp("CDABCDABCDB", "CDABCDB"))
	fmt.Println(kmp("CDABCDABCDB", "AB"))
	fmt.Println(kmp("CDABCDABCDB", "ABCDB"))
}
