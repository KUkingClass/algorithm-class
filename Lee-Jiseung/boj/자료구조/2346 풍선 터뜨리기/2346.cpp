#include <iostream>
#include <vector>

using namespace std;
// 2022 09 17 16 31
// 2022 09 17 17 03


int main() {
    // boj 10866

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<pair<int, int>> v(n, { 0,0 });
    for (int i = 0; i < n; i++) {
        v[i].first = i + 1;
        cin >> v[i].second;
    }
    
    int cur = 0;
    vector<int> answer;
    
    while (--n) {
        answer.push_back(v[cur].first);
        int next = cur + v[cur].second;
        if (next > cur) next--;
        v.erase(v.begin() + cur);
        cur = next % n;
        if (cur < 0) cur += n;
    }
    answer.push_back(v[0].first);

    for (int i = 0; i < answer.size(); i++)
        cout << answer[i] << ' ';
    return 0;
}