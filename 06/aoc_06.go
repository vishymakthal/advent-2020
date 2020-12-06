package main

import (
	"bufio"
	"fmt"
	"os"
)

func solvePart1(group []string) int {
	set := make(map[byte]int)
	for _, g := range group {
		for i := range g {
			set[g[i]] = 1
		}
	}

	return len(set)
}

func solvePart2(group []string) int {
	freq := make(map[byte]int)
	cnt := 0

	for _, g := range group {
		for i := range g {
			if _, ok := freq[g[i]]; ok {
				freq[g[i]]++
			} else {
				freq[g[i]] = 1
			}
		}
	}

	for _, v := range freq {
		if v == len(group) {
			cnt++
		}
	}

	return cnt
}

func main() {

	// file open & close
	f, _ := os.Open("./in.txt")
	defer func() {
		f.Close()
	}()

	s := bufio.NewScanner(f)
	var group []string
	ans1 := 0
	ans2 := 0
	for s.Scan() {

		ln := s.Text()
		if ln == "" {
			ans1 += solvePart1(group)
			ans2 += solvePart2(group)
			group = []string{}

		} else {
			group = append(group, ln)
		}

	}

	fmt.Printf("Ans part 1: %d\n", ans1)
	fmt.Printf("Ans part 2: %d\n", ans2)
}
