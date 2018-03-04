package main

import "fmt"

/*
https://leetcode.com/problems/next-permutation
 */

func nextPermutation(nums []int) {
	n := len(nums)
	i := n - 1
	for ; i > 0; i-- {
		if nums[i] > nums[i-1] {
			break
		}
	}
	if i != 0 {
		j := i
		for ; j<n-1; j++ {
			if nums[j+1] <= nums[i-1] {
				break
			}
		}
		nums[i-1], nums[j] = nums[j], nums[i-1]
	}
	for j, k := i, n-1; j < k; j++ {
		nums[j], nums[k] = nums[k], nums[j]
		k--
	}
}

func main() {
	for _, nums := range [][]int{{1,2,0,3,7,6,5}, {2,3,1}, {1,5,1}} {
		nextPermutation(nums)
		fmt.Println(nums)
	}
}
