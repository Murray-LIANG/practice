package main

import "fmt"

/**
 * https://leetcode.com/problems/range-sum-query-immutable
 * Use a new array (or modify the nums array) to store the info of sum, for
 * example, new_array[i] = sum(nums[0], nums[1], ..., nums[i]). So the SumRange
 * from i to j is: new_array[j] - new_array[i].
 */
type NumArray struct {
	nums []int
	sums []int
}


func Constructor(nums []int) NumArray {
	if len(nums) == 0 {
		return NumArray{}
	}
	sums := []int{nums[0]}
	for i:=1; i<len(nums); i++{
		sums = append(sums, sums[i-1] + nums[i])
	}
	return NumArray{nums, sums}
}


func (this *NumArray) SumRange(i int, j int) int {
	if i == 0 {
		return this.sums[j]
	}
	return this.sums[j] - this.sums[i-1]
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(i,j);
 */

func main() {
	obj := Constructor([]int{-2,0,3,-5,2,-1})
	fmt.Println(obj.SumRange(2,5))
	fmt.Println(obj.SumRange(0,5))

}
