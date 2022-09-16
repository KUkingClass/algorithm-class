#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;
// 2022 09 13 17 42
// 2022 09 13 19 06

bool flag = true;

bool comp(pair<int, int> p1, pair<int, int> p2) {
    if (p1.first - p1.second == p2.first - p2.second) {
        flag = false;
        return p1.first + p1.second < p2.first + p2.second;
    }
    return p1.first - p1.second < p2.first - p2.second;
}

int main() {
    // boj 22942
    
    int n;
    cin >> n;
    
    vector<pair<int, int>> v(n, { 0,0 });
    for (int i = 0; i < n; i++) {
        cin >> v[i].first;
        cin >> v[i].second;
    }

    sort(v.begin(), v.end(), comp);

    deque<int> d(1, v[0].first + v[0].second);
    for (int i = 1; i < n && flag; i++) {
        int left = v[i].first - v[i].second;
        int right = v[i].first + v[i].second;

        while (!d.empty()) {
            if (d.front() == left) {
                flag = false;
                break;
            }
            else if (d.front() < left) {
                d.pop_front();
            }
            else {
                if (d.front() <= right) {
                    flag = false;
                }
                else {
                    d.push_front(right);
                }
                break;
            }
        }
    }

    if (flag) cout << "YES";
    else cout << "NO";
    return 0;
}