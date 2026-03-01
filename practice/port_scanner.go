package main

import (
    "fmt"
    "net"
    "sync"
    "time"
)

func scanPort(host string, port int, wg *sync.WaitGroup, results chan<- int) {
    defer wg.Done()
    address := fmt.Sprintf("%s:%d", host, port)
    conn, err := net.DialTimeout("tcp", address, 1*time.Second)
    if err == nil {
        results <- port
        conn.Close()
    }
}

func main() {
    host := "scanme.nmap.org"
    var wg sync.WaitGroup
    results := make(chan int, 100)

    for port := 1; port <= 1024; port++ {
        wg.Add(1)
        go scanPort(host, port, &wg, results)
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    fmt.Printf("Open ports on %s:\n", host)
    for port := range results {
        fmt.Printf("Port %d is open\n", port)
    }
}