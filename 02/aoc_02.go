package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func validatePart1(rng, char, pass string) bool {

	lStr := strings.Split(rng, "-")[0]
	uStr := strings.Split(rng, "-")[1]

	lower, _ := strconv.Atoi(lStr)
	upper, _ := strconv.Atoi(uStr)

	cnt := strings.Count(pass, char)

	return cnt >= lower && cnt <= upper
}

func validatePart2(rng, char, pass string) bool {

	lStr := strings.Split(rng, "-")[0]
	uStr := strings.Split(rng, "-")[1]

	lower, _ := strconv.Atoi(lStr)
	upper, _ := strconv.Atoi(uStr)

	if pass[lower-1] == char[0] {
		return pass[upper-1] != char[0]
	}

	return pass[upper-1] == char[0]

}

func main() {
	f, _ := os.Open("./pass.txt")
	defer func() {
		f.Close()
	}()

	validPart1 := 0
	validPart2 := 0
	s := bufio.NewScanner(f)
	for s.Scan() {
		parts := strings.Split(s.Text(), ":")

		pat := parts[0]
		pass := strings.TrimSpace(parts[1])
		patParts := strings.Split(pat, " ")

		if validatePart1(patParts[0], patParts[1], pass) {
			validPart1++
		}
		if validatePart2(patParts[0], patParts[1], pass) {
			validPart2++
		}
	}

	fmt.Printf("Ans part 1: %d\n", validPart1)
	fmt.Printf("Ans part 2: %d\n", validPart2)

}
