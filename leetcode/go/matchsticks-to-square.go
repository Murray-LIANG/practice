package main

import (
	"sort"
	"fmt"
)

/*
https://leetcode.com/problems/matchsticks-to-square

Set the length of square is X, then 4X = SUM. That is SUM % 4 == 0. We need to
put all nums into 4 sets, sum of each set should be X. So for each nums[I], we
try to put into 4 sets one by one. If all sum of 4 sets exceeds X, then return
false. If sum after adding nums[I] in any of 4 sets doesn't exceed X, then put
nums[I] into that set, and continue with nums[I+1]. The end condition is all
numbers in nums are put into any of 4 sets and the sums of 4 sets are equal.
 */

func makesquare(nums []int) bool {
	if len(nums) < 4 {
		return false
	}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%4 != 0 {
		return false
	}

	sort.Ints(nums)

	target := sum / 4
	sums := make([]int, 4)
	var dfs func(int) bool
	dfs = func(index int) bool {
		// From nums' end to front, that is use desc order of number in nums,
		// which will make the dfs fail quickly. Refer to line 43.
		if index == -1 {
			return sums[0] == sums[1] && sums[1] == sums[2]
		}
		for i := 0; i < 4; i++ {
			if sums[i]+nums[index] > target {
				continue
			}
			sums[i] += nums[index]
			if dfs(index - 1) {
				return true
			}
			sums[i] -= nums[index]
		}
		return false
	}
	return dfs(len(nums) - 1)
}

func main() {
	fmt.Println(makesquare([]int{1, 1, 2, 2, 2}))
	fmt.Println(makesquare([]int{1, 1, 1, 1, 2, 4, 3, 2, 1}))
	fmt.Println(makesquare([]int{7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205, 9922998}))
}
