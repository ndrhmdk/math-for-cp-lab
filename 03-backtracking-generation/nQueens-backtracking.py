def init(a, b, c, n):
    for i in range(1, n + 1):
        a[i] = 1
    for i in range(2, 2 * n + 1):
        b[i] = 1
    for i in range(1 - n, n):
        c[i] = 1

def out(x, n):
    global count
    count += 1
    print(f"{count}:\t", end="")
    for i in range(1, n + 1):
        print(f"{x[i]:3d}", end="")
    print()

def try_combinations(i, x, a, b, c, n):
    for j in range(1, n + 1):
        if a[j] == 1 and b[i + j] == 1 and c[i - j] == 1:
            x[i] = j
            a[j] = 0
            b[i + j] = 0
            c[i - j] = 0

            if i == n:
                out(x, n)
            else:
                try_combinations(i + 1, x, a, b, c, n)

            a[j] = 1
            b[i + j] = 1
            c[i - j] = 1

def main():
    n = 8
    a = [0] * (n + 1)
    b = [0] * (2 * n + 1)
    c = [0] * (2 * n - 1)
    x = [0] * (n + 1)

    global count
    count = 0

    init(a, b, c, n)
    try_combinations(1, x, a, b, c, n)

if __name__ == "__main__":
    main()