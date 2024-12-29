def init(n):
    return [1] * n

def out(s):
    global count
    print(f"{count}:  ", end="")
    for i in range(n):
        print(f"{s[i]}  ", end="")
    count += 1
    print()

def try_permutations(i, b, s):
    for j in range(n):
        if b[j] == 1:
            s[i] = j + 1
            b[j] = 0
            if i == n - 1:
                out(s)
            else:
                try_permutations(i + 1, b, s)
            b[j] = 1

def main():
    global n
    global count
    count = 1
    n = int(input("input n: "))
    b = init(n)
    s = [0] * n
    try_permutations(0, b, s)

if __name__ == "__main__":
    main()
