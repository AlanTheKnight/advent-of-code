package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func solvePart1(a1, a2, b1, b2 int) bool {
	return (a1 <= b1 && a2 >= b2) || (b1 <= a1 && b2 >= a2)
}

func solvePart2(a1, a2, b1, b2 int) bool {
	return min(a2, b2) - max(a1, b1) > -1
}

func main() {
	f, err := os.Open("input/day4.input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	cnt1 := 0
	cnt2 := 0

	for scanner.Scan() {
		line := scanner.Text()
		pairs := strings.Split(line, ",")
		t1 := strings.Split(pairs[0], "-")
		t2 := strings.Split(pairs[1], "-")
		a1, _ := strconv.Atoi(t1[0])
		a2, _ := strconv.Atoi(t1[1])
		b1, _ := strconv.Atoi(t2[0])
		b2, _ := strconv.Atoi(t2[1])
		if solvePart1(a1, a2, b1, b2) {
			cnt1++
		}
		if solvePart2(a1, a2, b1, b2) {
			cnt2++
		}
	}

	fmt.Println(cnt1)
	fmt.Println(cnt2)
}
