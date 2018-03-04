package main

import "fmt"

/*
https://leetcode.com/problems/burst-balloons

As normal thinking, you could try this way:
burst balloon I, then calculate the max coins count to burst other N - 1
balloons, that is, for each I in 0 ~ N-1, we check that the total coins we can
get when we burst balloon I,
coins[0][N-1] = nums[I-1] * nums[I] * nums[I+1] + coins[0][N-2]
(one balloon less)
As in dp, we could use memorization here, but the problem is that when bursting
I, the coins you get would be different based on the left and right neighbors.

So here comes the most difficult part of this problem, reverse thinking.
That is, taking balloon I as the last balloon in all N balloons. As above,
in this way, the left and right neighbors are easy to know (they are both 1).
For each I in 0 ~ N-1, we check that the total coins we can get
when you know balloon I is the last to burst,
coins[0][N-1] = nums[0] * nums[I] * nums[N-1] + coins[0][I] + coins[I][N-1]
(taking I into count to each side, because I is the last balloon to burst)
 */

func maxCoins(nums []int) int {
	// `nums` is [1, ...nums..., 1] now. Length is the old one + 2.
	nums = append([]int{1}, nums...)
	nums = append(nums, 1)
	n := len(nums)
	memo := make([][]int, n)
	for i := 0; i < n; i++ {
		memo[i] = make([]int, n)
	}

	var dp func(int, int) int
	dp = func(start int, end int) int {
		// nums from start to end (including) should be at least 3.
		if end-start < 2 {
			return 0
		}

		if memo[start][end] != 0 {
			return memo[start][end]
		}

		max := 0
		for i := start + 1; i < end; i++ {
			tmp := nums[start]*nums[i]*nums[end] + dp(start, i) + dp(i, end)
			if tmp > max {
				max = tmp
			}
			memo[start][end] = max
		}
		return max
	}
	return dp(0, n-1)
}

func main() {
	fmt.Println(maxCoins([]int{3,1,5,8}))
}
