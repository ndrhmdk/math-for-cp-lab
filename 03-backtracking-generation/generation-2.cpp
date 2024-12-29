#include <stdio.h>
#include <iostream>

using namespace std;

void init(int a[], int k) {
    for (int i = 0; i < k; i++) {
        a[i] = i + 1;
    }
}

void out(int a[], int k) {
    for (int i = 0; i < k; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

void gen(int a[], int k, int n) {
    int i = k - 1;
    while (i >= 0 && a[i] == n - k + i + 1) {
        i--;
    }

    if (i >= 0) {
        a[i]++;
        for (int j = i + 1; j < k; j++) {
            a[j] = a[i] + j - i;
        }
    }
}

int islast(int a[], int k, int n) {
    for (int i = 0; i < k; i++) {
        if (a[i] != n - k + i + 1) return 0;
    }
    return 1;
}

void method(int a[], int n, int k) {
    init(a, k);
    out(a, k);
    int stop = islast(a, k, n);
    while (stop == 0) {
        gen(a, k, n);
        out(a, k);
        stop = islast(a, k, n);
    }
}

int main() {
    int k, n;
    cout << "Input n: ";
    cin >> n;
    cout << "Input k: ";
    cin >> k;
    int a[k];
    method(a, n, k);
    return 0;
}