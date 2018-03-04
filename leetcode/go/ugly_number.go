package main

/*
https://leetcode.com/problems/ugly-number

Divided N by 2 until N % 2 != 0, then divided the new N by 3 until N % 3 != 0,
finally divided the new N by 5 until N % 5 != 0. If the left N is not 1, then
it is ugly.
 */


func isUgly(num int) bool {
	for ; num%2 == 0 && num > 0; num /= 2 {
	}
	for ; num%3 == 0 && num > 0; num /= 3 {
	}
	for ; num%5 == 0 && num > 0; num /= 5 {
	}

	return num == 1
}

func main() {
}
