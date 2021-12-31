package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func readFileContents() {
	bytes, err := os.ReadFile("data.txt")
	if err != nil {
		log.Fatal(err)
	}
	fileText := string(bytes[:])

	lst := strings.Split(fileText, ";")

	for ind, num := range lst {
		if num == "0" {
			fmt.Println(ind + 1)
		}
	}
}

func main() {
	readFileContents()
}
