#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <string>

using namespace std;
// 2022 09 30 21 52
// 2022 09 30 22 33


int main() {
    // boj 16637

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string s;
    cin >> n >> s;

    if (n == 1) {
        cout << s[0] - '0';
        return 0;
    }

    vector<int> nums;
    vector<int> ops;
    for (int i = 0; i < s.length(); i++) {
        if (i & 1) {
            ops.push_back(s[i]);
        }
        else {
            nums.push_back(s[i] - '0');
        }
    }
    
    int answer = INT_MIN;
    for (int i = 0; i < (1 << ops.size()); i++) {
        bool flag = false;
        for (int j = 0; j < ops.size() - 1; j++) {
            if (i & (1 << j) && i & (1 << (j + 1))) {
                flag = true;
                break;
            }
        }
        if (flag) continue;

        vector<int> num = { nums.begin(), nums.end() };
        vector<int> op = { ops.begin(), ops.end() };
        for (int j = 0; j < op.size(); j++) {
            if (i & (1 << j)) {
                if (op[j] == 43) {
                    num[j] += num[j + 1];
                }
                else if (op[j] == 45) {
                    num[j] -= num[j + 1];
                }
                else {
                    num[j] *= num[j + 1];
                }
                op[j] = 43;
                num[j + 1] = 0;
            }
        }

        int result = num[0];
        for (int j = 0; j < op.size(); j++) {
            if (op[j] == 43) {
                result += num[j + 1];
            }
            else if (op[j] == 45) {
                result -= num[j + 1];
            }
            else {
                result *= num[j + 1];
            }
        }

        answer = max(result, answer);
    }

    cout << answer;
    return 0;
}