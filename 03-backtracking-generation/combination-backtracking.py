count = 1

def out(x):
    global count
    count += 1
    print(f"{count}:\t{' '.join(map(str, x))}")

def try_combinations(i, start, n, k, x):
    for j in range(start, n + 1):
        x[i] = j
        if i == k - 1:
            out(x)
        else:
            try_combinations(i + 1, j + 1, n, k, x)

def main():
    n = 5
    k = 3
    x = [0] * k
    try_combinations(0, 1, n, k, x)

if __name__ == '__main__':
    main()