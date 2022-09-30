#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;
// 2022 09 26 15 07
// 2022 09 26 15 14


int main() {
    // boj 1620

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<string> v(n, "");
    map<string, int> mp;
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        mp[v[i]] = i + 1;
    }

    while (m--) {
        string s;
        cin >> s;

        if ('0' <= s[0] && s[0] <= '9') 
            cout << v[stoi(s) - 1] << '\n';
        else 
            cout << mp[s] <<'\n';
    }

    return 0;
  }