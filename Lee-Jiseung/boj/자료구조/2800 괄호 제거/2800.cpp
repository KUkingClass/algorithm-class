#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;
// 2022 09 17 14 25
// 2022 09 17 14 46


int main() {
    // boj 2800

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    deque<int> open;
    vector<pair<int, int>> v;
    vector<string> answer;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') open.push_back(i);
        else if (s[i] == ')') {
            v.push_back({ open.back(), i });
            open.pop_back();
        }
    }

    int n = v.size();
    for (int i = 1; i < (1 << n); i++) {
        string temp = s;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                temp[v[j].first] = ' ';
                temp[v[j].second] = ' ';
            }
        }

        int index = 0;
        while (index < temp.length()) {
            if (temp[index] == ' ') {
                temp.erase(index, 1);
            }
            else index++;
        }
        
        answer.push_back(temp);
    }
    
    sort(answer.begin(), answer.end());
    answer.erase(unique(answer.begin(), answer.end()), answer.end());
    
    for (int i = 0; i < answer.size(); i++) cout << answer[i] << '\n';

    return 0;
}