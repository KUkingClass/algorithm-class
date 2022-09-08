#include <iostream>
#include <vector>

using namespace std;
// 2022 09 07 23 33
// 2022 09 07 23 42

int main() {
    // boj 1316

    int n;
    cin >> n;

    int answer = 0;
    while (n--) {
        string s;
        cin >> s;

        vector<bool> v(26, false);
        int prev = -1;
        for (int i = 0; i < s.length(); i++) {
            int c = s[i] - 'a';
            if (c != prev) {
                if (v[c]) {
                    prev = -1;
                    break;
                }
                else {
                    v[c] = true;
                    prev = c;
                }
            }
        }

        if (prev != -1) answer++;
    }

    cout << answer;
    return 0;
}
