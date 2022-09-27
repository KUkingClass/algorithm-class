#include <iostream>
#include <vector>
#include <map>

using namespace std;
// 2022 09 26 17 34
// 2022 09 26 17 37


int main() {
    // boj 14425

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    map<string, int> mp;
    while (n--) {
        string s;
        cin >> s;

        mp[s] = n;
    }

    int answer = 0;
    while (m--) {
        string s;
        cin >> s;

        if (mp.find(s) != mp.end())
            answer++;
    }

    cout << answer;
    return 0;
}