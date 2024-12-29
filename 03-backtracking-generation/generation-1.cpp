#include <iostream>
using namespace std;

void init(int b[], int n) {
    for (int i = 0; i < n; i++) b[i] = 0;
}

void out(int b[], int n) {
    for (int i = 0; i < n; i++) cout << b[i] << " ";
    cout << endl;
}

int islast(const int b[], int n) {
    for (int i = 0; i < n; i++) if (b[i] == 0) return 0;
    return 1;
}

void gen(int b[], int n) {
    int i = n - 1;
    while (i >= 0 && b[i] == 1) i--;
    if (i >= 0) {
        b[i] = 1;
        for (int j = i + 1; j < n; j++) b[j] = 0;
    }
}

void method(int b[], int n) {
    init(b, n);
    out(b, n);
    int stop = islast(b, n);
    while (stop == 0) {
        gen(b, n);
        out(b, n);
        stop = islast(b, n);
    }
}

int main() {
    int n = 4;
    int b[n];
    method(b, n);
    return 0;
}