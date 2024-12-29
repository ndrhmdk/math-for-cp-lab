#include<stdio.h>

int n, count = 1;

void init(int b[]) {
    int j;
    for (j = 1; j <= n; j++) b[j] = 1;
}

void out(int s[]) {
    printf("%d:  ", count);
    int i;
    for (i = 1; i <= n; i++) printf("%d  ", s[i]);
    count++;
    printf("\n");
}

void Try(int i, int b[], int s[]) {
    int j;
    for (j = 1; j <= n; j++) {
        if (b[j] == 1) {
            s[i] = j;
            b[j] = 0;
            if (i == n) out(s);
            else Try (i + 1, b, s);
            b[j] = 1;
        }
    }
}

int main() {
    printf("input n: ");
    scanf("%d", &n);
    int b[n], s[n];
    init(b);
    Try(1, b, s);
}