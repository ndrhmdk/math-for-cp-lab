count = 1

def out(s, n):
    global count
    print(f"{count}: ", end="")
    count += 1
    for i in range(1, n + 1):
        print(f"{s[i]:3d}", end="")
    print()

def Try(i, s, b, n):
    for j in range(1, n + 1):
        if b[j] == 1:
            s[i] = j
            b[j] = 0
            if i == n:
                out(s, n)
            else:
                Try(i + 1, s, b, n)
            b[j] = 1

def main():
    n = 5
    b = [1] * (n + 1)
    s = [0] * (n + 1)
    Try(1, s, b, n)

if __name__ == "__main__":
    main()