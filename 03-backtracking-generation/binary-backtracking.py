count = 1

def out(b, n):
    global count
    print(f"{count}:\t", end='')
    count += 1
    for i in range(1, n + 1):
        print(b[i], end=" ")
    print()

def Try(i, s, n):
    for j in range(2): # 0 and 1
        s[i] = j
        if i == n:
            out(s, n)
        else:
            Try(i + 1, s, n)

def main():
    n = 8
    s = [0] * (n + 1)
    Try(1, s, n)

if __name__ == "__main__":
    main()