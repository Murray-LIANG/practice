package main

import "fmt"

/*
https://leetcode.com/problems/super-pow

a^123456 %k = (a^123450 * a^6) %k = (a^123450 %k) * (a^6 %k) %k
= (a^12345 %k)^10 %k * (a^6 %k) %k
a^123456 %k = f(a,123456) = f(a,12345)^10 %k * f(a,6) %k
= f(f(a,12345),10) * f(a,6) %k
Because b is in an array, and every number not greater than 10, we could use
recursion to solve f(a,b) until b is empty list.
And we need another function to calculate the f(a,b) when b is single number.
 */

func mod_1337(a int, b int) int {
	if b == 0 {
		return 1
	}
	return (mod_1337(a, b-1) * a % 1337) % 1337
}

func superPow(a int, b []int) int {
	if len(b) == 0 {
		return 1
	}
	last := b[len(b)-1]
	b = b[:len(b)-1]
	return (mod_1337(superPow(a, b), 10) * mod_1337(a, last)) % 1337
}

func main() {
	fmt.Println(superPow(2, []int{1,0}))
}
