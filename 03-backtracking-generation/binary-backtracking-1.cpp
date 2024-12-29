#include <stdio.h>
int count = 1;

void out(int b[], int n) {
    printf("%d:  ", count);
    count++;
    for (int i = 1; i <= n; i++) {
        printf("%d ", b[i]); 
    }
    printf("\n");
}

void Try(int i, int s[], int n) {
    for (int j = 0; j <= 1; j++) { 
        s[i] = j;
        if (i == n) {
            out(s, n);
        } else {
            Try(i + 1, s, n);
        }
    }
}

int main() {
    int n;
    printf("input n: ");
    scanf("%d", &n);
    int s[n + 1];
    Try(1, s, n);
    return 0;
}
