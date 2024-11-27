def init(b, n):
    for i in range(n):
        b.append(0)

def out(b, n):
    print("".join(map(str, b[:n])))

def islast(b, n):
    return all(x == 1 for x in b[:n])

def gen(b, n):
    i = n - 1
    while i >= 0 and b[i] == 1:
        i -= 1
    if i >= 0:
        b[i] = 1
        for j in range(i + 1, n):
            b[j] = 0

def method(b, n):
    init(b, n)
    out(b, n)
    while not islast(b, n):
        gen(b, n)
        out(b, n)

def main():
    n = 4
    b = []
    method(b, n)

if __name__ == "__main__":
    main()