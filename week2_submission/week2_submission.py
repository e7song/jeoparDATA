import sys

def fibonacci(n):
    # base cases
    if n == 0 or n == 1:
        return n
    else:
        prev, curr = 0, 1
        for _ in range(2, n):
            next = prev + curr
            prev = curr
            curr = next
        return curr
    
def linear_fibonacci(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    else:
        fib = [0] * n
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n):
            fib[i] = fib[i - 1] + fib[i - 2]
    return fib



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("format: py week2_submission.py [number]")
    input = int(sys.argv[1])
    print(fibonacci(input))
    print(linear_fibonacci(input))

