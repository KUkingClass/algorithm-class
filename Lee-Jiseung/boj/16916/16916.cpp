#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
// 2022 09 08 15 42
// 2022 09 11 00 52


int main() {
    // boj 16916

    string str;
    cin >> str;

    string s;
    cin >> s;

    vector<int> v(s.length(), 0);
    int j = 0;
    for (int i = 1; i < s.length(); i++) {
        while (j > 0 && s[i] != s[j]) {
            j = v[j - 1];
        }
        if (s[i] == s[j]) {
            j++;
            v[i] = j;
        }
    }

    j = 0;
    for (int i = 0; i < str.length(); i++) {

        while (j > 0 && str[i] != s[j]) {
            j = v[j - 1];
        }
        if (str[i] == s[j]) {
            if (j == s.length() - 1) {
                cout << 1;
                return 0;
            }
            else {
                j++;
            }
        }
    }

    cout << 0;
    return 0;
}