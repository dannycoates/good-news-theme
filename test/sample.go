// Package main demonstrates Go syntax highlighting
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"sync"
	"time"
)

// Constants
const (
	MaxRetries    = 3
	DefaultTimeout = 30 * time.Second
)

// Custom type
type Status int

const (
	StatusPending Status = iota
	StatusActive
	StatusInactive
)

// Interface definition
type Repository interface {
	Get(ctx context.Context, id string) (*User, error)
	Save(ctx context.Context, user *User) error
}

// Struct with tags
type User struct {
	ID        string    `json:"id" db:"id"`
	Name      string    `json:"name" db:"name"`
	Email     string    `json:"email,omitempty" db:"email"`
	CreatedAt time.Time `json:"created_at" db:"created_at"`
	metadata  map[string]interface{}
}

// Constructor function
func NewUser(name, email string) *User {
	return &User{
		ID:        generateID(),
		Name:      name,
		Email:     email,
		CreatedAt: time.Now(),
		metadata:  make(map[string]interface{}),
	}
}

// Method with pointer receiver
func (u *User) SetMetadata(key string, value interface{}) {
	u.metadata[key] = value
}

// Method with value receiver
func (u User) String() string {
	return fmt.Sprintf("User{ID: %s, Name: %s}", u.ID, u.Name)
}

// Generic function (Go 1.18+)
func Filter[T any](items []T, predicate func(T) bool) []T {
	result := make([]T, 0)
	for _, item := range items {
		if predicate(item) {
			result = append(result, item)
		}
	}
	return result
}

// Goroutine and channels
func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(100 * time.Millisecond)
		results <- job * 2
	}
}

// Error handling
func fetchData(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("failed to fetch: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status: %d", resp.StatusCode)
	}

	return io.ReadAll(resp.Body)
}

func main() {
	// Variables
	var name string = "Go"
	count := 42
	pi := 3.14159
	isEnabled := true
	var nothing *string = nil

	// Slices and maps
	numbers := []int{1, 2, 3, 4, 5}
	config := map[string]interface{}{
		"host":    "localhost",
		"port":    8080,
		"enabled": true,
	}

	// Control flow
	for i, n := range numbers {
		if n%2 == 0 {
			fmt.Printf("Index %d: %d is even\n", i, n)
		} else {
			fmt.Printf("Index %d: %d is odd\n", i, n)
		}
	}

	// Switch statement
	switch status := StatusActive; status {
	case StatusPending:
		fmt.Println("Pending")
	case StatusActive:
		fmt.Println("Active")
	default:
		fmt.Println("Unknown")
	}

	// Type switch
	var value interface{} = "hello"
	switch v := value.(type) {
	case string:
		fmt.Printf("String: %s\n", v)
	case int:
		fmt.Printf("Int: %d\n", v)
	default:
		fmt.Printf("Unknown type: %T\n", v)
	}

	// Defer
	defer fmt.Println("Cleanup")

	// Goroutines and channels
	jobs := make(chan int, 100)
	results := make(chan int, 100)
	var wg sync.WaitGroup

	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go worker(w, jobs, results, &wg)
	}

	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println("Result:", result)
	}

	// Anonymous function
	add := func(a, b int) int {
		return a + b
	}
	fmt.Println(add(1, 2))

	_ = name
	_ = count
	_ = pi
	_ = isEnabled
	_ = nothing
	_ = config
}

func generateID() string {
	return "generated-id"
}
