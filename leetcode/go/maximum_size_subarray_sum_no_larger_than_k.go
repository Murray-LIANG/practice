package main

import (
	"fmt"
	"math"
)

/*
This problem is like the one `equal to k`.
In the `equal to k` problem, sum(0..i) - sum(0..j) == k.
But in this one, it is sum(0..i) - sum(0..j) <= k,
sum(0..j) >= sum(0..i) - k, which means:
for each i, we need to calculate the sum(0..i), and find the minimal existing
sum(0..j) greater than or equal to sum(0..i)-k.
 */

func sumNoLargerThanK(nums []int, k int) int {
	// sums is designed as:
	// sums[0] = sum([])
	// sums[1] = sum(nums[0])
	// sums[2] = sum(nums[0..1])
	sums := []int{0}

	sum, max := 0, 0

	for _, v := range nums {
		sum += v
		if s, ok := searchCeiling(nums, sum-k); ok && sum-s > max {
			max = sum - s
		}
		sums = append(sums, sum)
	}
	return max
}

func searchCeiling(nums []int, num int) (int, bool) {
	res := math.MaxInt32
	for _, v := range nums {
		if v < num {
			continue
		}
		if v-num < res {
			res = v - num
		}
	}
	if res == math.MaxInt32 {
		return res, false
	} else {
		return res + num, true
	}
}

func main() {
	nums := []int{1, 0, 1, 0, -2, 3}
	fmt.Println(sumNoLargerThanK(nums, 4))
}
