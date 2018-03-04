package main

import (
	"strings"
	"strconv"
	"fmt"
)

/*
https://leetcode.com/problems/exclusive-time-of-functions

Because the jobs are executed in a nonpreemptive single threaded CPU,
this problem can be solved by using stack.
 */

func exclusiveTime(n int, logs []string) []int {
	res := make([]int, n)
	stack := []int{}
	preTime := 0
	for _, log := range logs {
		parts:=strings.Split(log, ":")
		funcId, _ := strconv.Atoi(parts[0])
		time, _ := strconv.Atoi(parts[2])
		if parts[1] == "start" {
			if len(stack) != 0 {
				res[stack[len(stack)-1]] += time - preTime
			}
			stack = append(stack, funcId)
			preTime = time
		} else {
			res[stack[len(stack)-1]] += time - preTime + 1
			stack = stack[:len(stack)-1]
			preTime = time + 1
		}
	}
	return res
}

func main() {
	logs := []string{
		"0:start:0",
		"1:start:2",
		"1:end:5",
		"0:end:6",
	}
	fmt.Println(exclusiveTime(2, logs))
}
