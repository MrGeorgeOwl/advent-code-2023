package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type game struct {
	Id       int
	MaxRed   int
	MaxGreen int
	MaxBlue  int
}

func (g game) String() string {
	return fmt.Sprintf("{id: %v, red: %v, green: %v, blue: %v}", g.Id, g.MaxRed, g.MaxGreen, g.MaxBlue)
}

var cube = regexp.MustCompile(`(\d+)\s+(blue|red|green)`)

func main() {
	games, err := parseGamesFile()
	if err != nil {
		log.Fatal(err)
	}

	filtered := filterGamesWithUpperBound(games, 12, 13, 14)
	var idSum int
	for _, item := range filtered {
		idSum += item.Id
	}

	fmt.Println("sum of ids with possible amount of cubes (1 part)", idSum)

	var productSum int
	for _, item := range games {
		product := item.MaxRed * item.MaxGreen * item.MaxBlue
		productSum += product
	}

	fmt.Println("sum of products (2 part): ", productSum)
}

func parseGamesFile() ([]game, error) {
	f, err := os.Open("input.txt")
	if err != nil {
		return nil, fmt.Errorf("parseGamesFile: reading file: %s", err)
	}
	defer f.Close()

	games := make([]game, 0)
	scanner := bufio.NewScanner(f)
	counter := 1
	for scanner.Scan() {
		g := game{Id: counter}
		line := scanner.Text()
		err := parseLine(&g, line)
		if err != nil {
			log.Fatalf("parseGamesFile: %s\n", err)
			continue
		}
		counter++
		games = append(games, g)
	}

	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("parseGamesFile: scanning file: %s", err)
	}

	return games, nil
}

func parseLine(g *game, line string) error {
	for _, v := range cube.FindAllString(strings.Split(line, ":")[1], -1) {
		splitted := strings.Split(v, " ")
		amount, err := strconv.Atoi(splitted[0])
		if err != nil {
			return fmt.Errorf("parseLine: %s, Subset: %s", err, v)
		}

		switch splitted[1] {
		case "red":
			if amount > g.MaxRed {
				g.MaxRed = amount
			}
		case "blue":
			if amount > g.MaxBlue {
				g.MaxBlue = amount
			}
		case "green":
			if amount > g.MaxGreen {
				g.MaxGreen = amount
			}
		}
	}

	return nil
}

func filterGamesWithUpperBound(games []game, r, g, b int) []game {
	filter := make([]game, 0)
	for _, item := range games {
		if item.MaxRed <= r && item.MaxGreen <= g && item.MaxBlue <= b {
			filter = append(filter, item)
		}
	}

	return filter
}
