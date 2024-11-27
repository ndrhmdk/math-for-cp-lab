def out(x, k):
    global count
    count += 1
    print(f"{count}:\t", end="")
    for i in range(1, k + 1):
        print(f"{x[i]:3d}", end="")
    print()

def Try(i, sum, n, k, x):
    for j in range(n + 1):
        x[i] = j
        if i == k:
            if sum + j == n:
                out(x, k)
        else:
            Try(i + 1, sum + j, n, k, x)

def main():
    global count
    count = 0
    n = int(input("Input n (target number): "))
    k = int(input("Input k (length of sequence): "))
    x = [0] * (k + 1)
    print("Solutions:")
    Try(1, 0, n, k, x)

if __name__ == "__main__":
    main()