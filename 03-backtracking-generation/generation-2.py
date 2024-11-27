def init(a, k):
    for i in range(k):
        a.append(i + 1)

def out(a, k):
    print(" ".join(map(str, a[:k])))

def gen(a, k, n):
    i = k - 1
    while i >= 0 and a[i] == n - k + i + 1:
        i -= 1

    if i >= 0:
        a[i] += 1
        for j in range(i + 1, k):
            a[j] = a[i] + j - i

def is_last(a, k, n):
    for i in range(k):
        if a[i] != n - k + i + 1:
            return False
    return True

def method(a, n, k):
    init(a, k)
    out(a, k)
    while not is_last(a, k, n):
        gen(a, k, n)
        out(a, k)

def main():
    n = int(input("Input n: "))
    k = int(input("Input k: "))
    a = []
    method(a, n, k)

if __name__ == "__main__":
    main()