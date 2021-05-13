package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("tex.txt")

	if err != nil {
		log.Fatal(err)
	}
	scaner := bufio.NewScanner(file)
	for scaner.Scan() {
		// fmt.Println(scaner.Text())
		// fmt.Println(reflect.TypeOf(scaner.Text()))
		value, err := strconv.ParseFloat(scaner.Text(), 64)
		if err != nil {
			panic(err)
		}
		fmt.Println(value)

	}
	err = file.Close()
	if err != nil {
		log.Fatal(err)
	}

}
