package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	target = 2020
)

func twoSum(nums []int) (int, int) {

	m := make(map[int]int)
	for _, n := range nums {
		if v, ok := m[n]; ok {
			return v, n
		}
		m[target-n] = n
	}
	return 0, 0
}

func threeSum(nums []int) (int, int, int) {

	sort.Ints(nums)
	for i, n := range nums {
		left := i + 1
		right := len(nums) - 1
		for left < right {

			p := n + nums[left] + nums[right]
			if p < target {
				left++
			}
			if p > target {
				right--
			}
			if p == target {
				return n, nums[left], nums[right]
			}
		}
	}

	return 0, 0, 0
}

func main() {

	f, _ := os.Open("./nums.txt")
	defer func() {
		f.Close()
	}()

	s := bufio.NewScanner(f)
	var n []int
	for s.Scan() {
		i, _ := strconv.Atoi(s.Text())
		n = append(n, i)
	}

	a, b := twoSum(n)
	fmt.Printf("Ans Part 1: %d\n", a*b)

	x, y, z := threeSum(n)
	fmt.Printf("Ans Part 2: %d\n", x*y*z)
}
