package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func initSeen(start string) map[int][]int {

	var num int
	seen := make(map[int][]int)
	parts := strings.Split(start, ",")
	for i, n := range parts {

		// store num and last turn it was seen
		num, _ = strconv.Atoi(n)
		seen[num] = []int{i + 1}
	}
	return seen
}
func solvePart1(seen map[int][]int, maxTurn int) int {

	prev := 0
	for turn := len(seen) + 1; turn < maxTurn; turn++ {
		if last, ok := seen[prev]; ok {
			tmp := turn - last[0]
			seen[prev] = []int{turn, last[0]}
			prev = tmp
		} else {
			seen[prev] = []int{turn}
			prev = 0
		}
	}
	return prev
}

func main() {

	start := os.Args[1]
	maxTurn, _ := strconv.Atoi(os.Args[2])
	seen := initSeen(start)
	fmt.Printf("ans part 1: %d\n", solvePart1(seen, maxTurn))
}
