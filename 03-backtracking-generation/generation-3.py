def init(n):
    return list(range(1, n + 1))

def out(a):
    print(' '.join(map(str, a)))

def reverse(a, start):
    end = len(a) - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

def gen(a):
    k = -1
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i + 1]:
            k = i
            break
    if k == -1:
        return False

    l = -1
    for i in range(len(a) - 1, k, -1):
        if a[i] > a[k]:
            l = i
            break

    a[k], a[l] = a[l], a[k]
    reverse(a, k + 1)
    return True

def islast(a):
    return all(a[i] >= a[i + 1] for i in range(len(a) - 1))

def method(n):
    a = init(n)
    out(a)

    while gen(a):
        out(a)

def main():
    n = int(input("Input n: "))
    method(n)

if __name__ == "__main__":
    main()
