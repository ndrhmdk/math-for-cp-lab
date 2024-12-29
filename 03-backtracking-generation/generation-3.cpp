#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void init(vector<int>& a, int n) {
    for (int i = 0; i < n; ++i) {
        a[i] = i + 1;
    }
}

void out(const vector<int>& a) {
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;
}

void reverse(vector<int>& a, int start) {
    int end = a.size() - 1;
    while (start < end) {
        swap(a[start], a[end]);
        start++;
        end--;
    }
}

bool gen(vector<int>& a) {
    int k = -1;
    for (int i = a.size() - 2; i >= 0; --i)
        if (a[i] < a[i + 1]) {
            k = i;
            break;
        }
    if (k == -1) return false;

    int l = -1;
    for (int i = a.size() - 1; i > k; --i)
        if (a[i] > a[k]) {
            l = i;
            break;
        }
    
    swap(a[k], a[l]);
    reverse(a, k + 1);
    return true;
}

bool islast(const vector<int>& a) {
    for (size_t i = 0; i < a.size() - 1; ++i) 
        if (a[i] < a[i + 1]) 
            return false;
    return true;
}

void method(int n) {
    vector<int> a(n);
    init(a, n);
    out(a);

    while(gen(a)) out(a);
}

int main() {
    int n;
    cout << "Input n: ";
    cin >> n;
    method(n);
    return 0;
}