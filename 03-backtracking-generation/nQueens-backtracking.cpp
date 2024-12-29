#include<stdio.h>

int a[100], b[100], c[100], x[100];
int count = 0;

void init(int a[], int b[], int c[], int n) {
    for (int i = 1; i <= n; i++)
        a[i] = 1;
    for (int i = 2; i <= 2 * n; i++) 
        b[i] = 1;
    for (int i = 1 - n; i <= n - 1; i++)
        c[i] = 1;
}

void out(int a[], int n) {
    printf("%d: ", ++count);
    for (int i = 1; i <= n; i++) {
        printf("%3d", x[i]);
    }
    printf("\n");
}

void Try(int i, int x[], int a[], int b[], int c[], int n) {
    for (int j = 1; j <= n; j++) {
        if (a[j] == 1 && b[i + j] == 1 && c[i - j] == 1) {
            x[i] = j;
            a[j] = 0;
            b[i + j] = 0;
            c[i - j] = 0;
            
            if (i == n) {
                out(x, n);
            } else {
                Try(i + 1, x, a, b, c, n);
            }
            
            a[j] = 1;
            b[i + j] = 1;
            c[i - j] = 1;
        }
    }
}

int main() {
    int n;
    printf("n = ");
    scanf("%d", &n);
    if (n < 4) {
        printf("No solution.");
    } else {
        init(a, b, c, n);
    Try(1, x, a, b, c, n);
    }    
}
