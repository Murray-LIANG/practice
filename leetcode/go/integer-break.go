package main

import "fmt"

/*
https://leetcode.com/problems/integer-break

Use bottom up to solve this problem.
f(1) = 1 ---> Added for later computation.
f(2) = 1 ---> This value doesn't include the 2 itself.
f(3) = f(1+2) = max{f(1) * f(2), f(1) * 2, f(2) * f(1), f(2) * 1}
	 = max{ max{1,f(1)} * max{2,f(2)} }
f(5) = max{f(1+4), f(2+3)}
     = max{ max{1,f(1)} * max{4,f(4)}, max{2,f(2)} * max{3,f(3)} }
f(n) = max{ max{i,f(i)} * max{n-i,f(n-i)} } (1<=i<=n/2)
We could use an array to store the info of f, and set the boundary as f(2) = 1,
f(1) = 1. So we calculate the value of f from 3 to n.
 */

func integerBreak(n int) int {
	f := make([]int, n+1)
	f[1] = 1
	f[2] = 1

	var Max func(int, int) int
	Max = func(a int, b int) int {
		if a >= b {
			return a
		}
		return b
	}

	for k:=3; k <=n; k++{
		for i := 1; i <= k/2; i++ {
			f[k] = Max(f[k], Max(i, f[i]) * Max(k-i, f[k-i]))
		}
	}
	return f[n]
}

func main() {
	fmt.Println(integerBreak(10))
}
