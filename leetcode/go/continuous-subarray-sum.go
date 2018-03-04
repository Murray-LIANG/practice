package main

import "fmt"

/*
https://leetcode.com/problems/continuous-subarray-sum

If sum[0..i] % k == sum[0..j] % k, then sum[i+1..j] % k = 0
 */

func checkSubarraySum(nums []int, k int) bool {
	sum := 0
	known := map[int]int{0: -1}
	for i, num := range nums {
		sum += num
		if k != 0 {
			sum %= k
		}
		if j, ok := known[sum]; ok {
			if i-j >= 2 {
				return true
			}
		} else {
			known[sum] = i
		}
	}
	return false
}

func main() {
	fmt.Println(checkSubarraySum([]int{23, 2, 6, 4, 7}, 6))
	fmt.Println(checkSubarraySum([]int{23, 2, 6, 4, 7}, 0))
	fmt.Println(checkSubarraySum([]int{0, 0 }, 0))
}
