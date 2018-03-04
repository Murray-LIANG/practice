package main

import "fmt"

/*
Given an array nums and a target value k, find the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

Solution:
sum(j..i) == k, where 0<=j<=i
sum(0..i) - sum(0..j-1) == k
sum(0..i) - k == sum(0..j-1)
That is for each i, we need check whether sum(0..i)-k exists before or not.
If yes, calculate the length, compare with the current max one.
And keep record of the sum(0..i). So we need a map to store the sum(0..i).
 */

func maxSubArrayLen(nums []int, k int) int {

	sumMap := map[int]int{}
	sumMap[0] = -1  // need to store the sum == 0 with index -1
	sum, maxLen := 0, 0

	for i, v := range nums {
		sum += v
		if _, ok := sumMap[sum-k]; ok {
			currLen := i - sumMap[sum-k]
			if currLen > maxLen {
				maxLen = currLen
			}
		}
		if _, ok := sumMap[sum]; !ok {
			// Only update sumMap when sum is not in it, because the old index
			// makes the length longer.
			sumMap[sum] = i
		}
	}
	return maxLen
}

func main() {
	nums := []int{1, -1, 5, -2, 3}
	fmt.Println(maxSubArrayLen(nums, 3))
}
