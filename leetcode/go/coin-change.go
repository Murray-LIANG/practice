package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/coin-change
 */

func coinChange(coins []int, amount int) int {
	// top-down with memo
	memo := map[int]int{0: 0}

	var dp func(int) int
	dp = func(amount int) int {
		if _, ok := memo[amount]; !ok {
			minCoins := math.MaxInt32
			for _, coin := range coins {
				if coin <= amount {
					if dp(amount-coin) != -1 && minCoins > dp(amount-coin)+1 {
						minCoins = dp(amount-coin) + 1
					}
				}
			}
			if minCoins == math.MaxInt32 {
				memo[amount] = -1
			} else {
				memo[amount] = minCoins
			}
		}
		return memo[amount]
	}
	return dp(amount)
}

func coinChange2(coins []int, amount int) int {
	// bottom up
	/* Set dp is the array to store the min coins related to each amount.
	 * Initially, dp[0] = 0. Like traversing the tree level by level, we get
	 * dp[1] = dp[0] + 1, dp[2] = dp[0] + 1, dp[5] = dp[0] + 1.
	 * Then dp[3] = dp[1+2] = dp[1] + 1 ...
	 * That is, based on the known value in dp to calculate the afterward ones.
	 */

	dp := make([]int, amount+1)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 0
	for i, v := range dp {
		if v != -1 {
			for _, coin := range coins {
				if (i + coin) <= amount {
					if dp[i+coin] == -1 || dp[i+coin] > v+1 {
						dp[i+coin] = v + 1
					}
				}
			}
		}
	}
	return dp[amount]
}

func main() {
	fmt.Println(coinChange2([]int{1, 2, 5}, 11))
}
