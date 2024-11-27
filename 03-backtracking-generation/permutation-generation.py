def printArr(arr, n, newline=True):
    print(" ".join(map(str, arr[:n])), end="")
    if newline:
        print()

# Generating permutation using Heap Algorithm
def heapPermutation(arr, n, size):
    if size == 1:
        printArr(arr, n)
        return

    for i in range(size):
        heapPermutation(arr, n, size-1)
        if size % 2 == 1:
            arr[0], arr[size-1] = arr[size-1], arr[0]  # swap first and last element
        else:
            arr[i], arr[size-1] = arr[size-1], arr[i]  # swap ith and last element

# Generating k-permutation using Heap Algorithm
def heapKPermutation(arr, n, k, size):
    if size == n - k + 1:
        printArr(arr[n - k:], k)
        return

    for i in range(size):
        heapKPermutation(arr, n, k, size-1)
        if size % 2 == 1:
            arr[0], arr[size-1] = arr[size-1], arr[0]  # swap first and last element
        else:
            arr[i], arr[size-1] = arr[size-1], arr[i]  # swap ith and last element

def doKCombination(arr, n, picked, k, size, start):
    if size == k:
        heapPermutation(picked, k, k)
    else:
        if start < n:
            doKCombination(arr, n, picked[:], k, size, start + 1)
            picked[size] = arr[start]
            doKCombination(arr, n, picked[:], k, size + 1, start + 1)

# Generate combination of k elements out of a set of n
def kCombination(arr, n, k):
    doKCombination(arr, n, [0] * k, k, 0, 0)

def main():
    arr = [1, 2, 3, 4, 5]
    kCombination(arr, len(arr), 5)

if __name__ == "__main__":
    main()