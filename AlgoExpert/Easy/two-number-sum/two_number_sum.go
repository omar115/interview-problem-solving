package main

import "fmt"

func TwoNumberSum(nums []int, target int) []int {
	for i, firstNum := range nums {
		for j := i + 1; j < len(nums); j++ {
			secondNum := nums[j]
			if firstNum+secondNum == target {
				return []int{firstNum, secondNum}
			}
		}
	}
	return []int{}
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	target := 5
	ans := TwoNumberSum(nums, target)
	fmt.Println(ans)
}
