package main

import "fmt"

type Number interface {
	int64 | float64
}

func SumInts(m map[string]int64) int64 {
	var s int64
	for _, v := range m {
		s += v
	}
	return s
}

func SumFloats(m map[string]float64) float64 {
	var s float64
	for _, v := range m {
		s += v
	}

	return s
}

func SumInsOrFloats[K comparable, V int64 | float64](m map[K]V) V {
	var s V
	for _, v := range m {
		s += v
	}
	return s
}

func SumNumbers[K comparable, V Number](m map[K]V) V {
	var s V
	for _, v := range m {
		s += v
	}
	return s
}

func main() {
	ints := map[string]int64 {
		"fitst":  34,
		"second": 12,
	}

	floats := map[string]float64 {
		"first":  35.98,
		"second": 26.99,
	}

	fmt.Printf("Non-Generic Sums: %v and %v\n",
		SumInts(ints),
		SumFloats(floats))

	fmt.Printf("Generic Sums: %v and %v\n",
		SumInsOrFloats[string, int64](ints),
		SumInsOrFloats[string, float64](floats))

	fmt.Printf("Generic Sums, type parameters inferred: %v and %v\n",
		SumInsOrFloats(ints),
		SumInsOrFloats(floats))

	fmt.Printf("Generic Sums with Constraint: %v and %v\n",
		SumNumbers(ints),
		SumNumbers(floats))
}