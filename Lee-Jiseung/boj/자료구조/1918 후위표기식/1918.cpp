#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 2022 09 13 16 14
// 2022 09 13 17 07


int main() {
    // boj 1918
    
    string s;
    cin >> s;
    
    int priority = 0;
    vector<string> nums;
    vector<pair<int, int>> ops; // priority & type
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') {
            priority++;
        }
        else if (s[i] == ')') {
            priority--;
        }
        else if (s[i] == '+') {
            ops.push_back({ priority, 0 });
        }
        else if (s[i] == '-') {
            ops.push_back({ priority, 1 });
        }
        else if (s[i] == '*') {
            ops.push_back({ priority, 2 });
        }
        else if (s[i] == '/') {
            ops.push_back({ priority, 3 });
        }
        else {
            nums.push_back(string(1, s[i]));
        }
    }

    while (!ops.empty()) {
        pair<int, int> mx = { -1, -1 };
        int index = 0;
        for (int i = 0; i < ops.size(); i++) {
            if (ops[i].first > mx.first) {
                mx = ops[i];
                index = i;
            }
            else if ((ops[i].first == mx.first) && (ops[i].second / 2 > mx.second / 2)) {
                mx = ops[i];
                index = i;
            }
        }
       
        string temp = nums[index] + nums[index + 1] + "+-*/"[ops[index].second];
        nums[index] = temp;
        nums.erase(nums.begin() + index + 1);
        ops.erase(ops.begin() + index);
    }

    cout << nums[0];
    return 0;
}