package main

import "fmt"

func maxSubArray(nums []int) int {
	maxLenIndex := make([]int, len(nums))
	maxI := nums[0]
	result := nums[0]
	resultIndex := 0
	for i := 1; i < len(nums); i++ {
		if maxI + nums[i] > nums[i] {
			maxI = maxI + nums[i]
			maxLenIndex[i] = maxLenIndex[i - 1]
		} else {
			maxI = nums[i]
			maxLenIndex[i] = i
		}
		if maxI > result {
			result = maxI
			resultIndex = i
		}
	}
	fmt.Println("Max sub array starts:", maxLenIndex[resultIndex])
	return result
}

/*
 We could define the problem as maxSubArray(A[], i, j), which means the
 maxSubArray for A[i:j]. In this way, our goal is to figure out what
 maxSubArray(A[], 0, len(A) - 1) is. However, in this way, it is hard to
 find the connection from the sub problem to the original problem.
 So we need to change the problem to maxSubArray(A[], i), which means the
 maxSubArray for A[0:i] having A[i] as the end element. This time the
 connection between sub problem and original problem is more clearer.
 maxSubArray(A[], i) = (maxSubArray(A[], i-1) < 0 ? 0 : maxSubArray(A[], i-1))
 		       + nums[i]
 */
func maxSubArrayDP(nums []int) int {
	n := len(nums)
	dp := make([]int, n)  // used to store maxSubArray(A[], i)

	dp[0] = nums[0]
	result := nums[0]

	for i := 1; i < n; i++ {
		if dp[i-1] > 0 {
			dp[i] = dp[i-1]+nums[i]
		} else {
			dp[i] = nums[i]
		}
		if dp[i] > result {
			result = dp[i]
		}
	}
	return result
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
	fmt.Println(maxSubArrayDP([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
