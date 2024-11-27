def init(a, n):
    for i in range(n):
        a.append(i + 1)

def out(a, n):
    print(" ".join(map(str, a[:n])))

def is_last(a, n):
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            return False
    return True

def gen(a, n):
    i = n - 2
    while i >= 0 and a[i] > a[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while a[j] < a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]

    a[i + 1:] = reversed(a[i + 1:])

def method(a, n):
    init(a, n)
    out(a, n)
    while not is_last(a, n):
        gen(a, n)
        out(a, n)

def main():
    n = int(input("input n: "))
    a = []
    method(a, n)

if __name__ == "__main__":
    main()