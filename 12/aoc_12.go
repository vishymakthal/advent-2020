package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	N = iota
	E
	S
	W
)

type Ship struct {
	x    int
	y    int
	card int
}

func (s *Ship) Execute(instruction string) {
	d := instruction[0]
	mag, _ := strconv.Atoi(instruction[1:])
	switch d {
	case 'F':
		switch s.card {
		case N:
			s.y += mag
		case S:
			s.y -= mag
		case E:
			s.x += mag
		case W:
			s.x -= mag
		}
	case 'R', 'L':
		inc := mag / 90
		if d == 'L' && (inc%2) != 0 {
			inc += 2
		}
		s.card = (s.card + inc) % 4
	case 'N':
		s.y += mag
	case 'S':
		s.y -= mag
	case 'E':
		s.x += mag
	case 'W':
		s.x -= mag
	}
}

func ReadInput(fname string) []string {
	var arr []string

	f, _ := os.Open(fname)
	defer func() {
		f.Close()
	}()

	s := bufio.NewScanner(f)
	for s.Scan() {
		arr = append(arr, s.Text())
	}
	return arr
}

func solve(inst []string) int {
	s := Ship{
		x:    0,
		y:    0,
		card: E,
	}

	for _, v := range inst {
		s.Execute(v)
	}

	return int(math.Abs(float64(s.x)) + math.Abs(float64(s.y)))
}

func main() {

	inst := ReadInput(os.Args[1])
	fmt.Printf("Ans: %d\n", solve(inst))
}
