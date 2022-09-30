#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
// 2022 09 30 20 59
// 2022 09 30 21 50


int main() {
    // boj 18511

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string n;
    int k;
    cin >> n >> k;
 
    vector<int> v(k, 0);
    int mx = 0;
    for (int i = 0; i < k; i++) {
        cin >> v[i];
        mx = max(v[i], mx);
    }
    sort(v.begin(), v.end());
    
    string answer(n.length() - 1, mx + '0');
    vector<int> index(n.length(), 0);
    while (true) {
        if (index[0] == k) break;

        string temp = "";
        for (int i = 0; i < index.size(); i++) {
            temp += v[index[i]] + '0';
        }
        if (n < temp) break;
        answer = temp;

        index[n.length() - 1]++;
        for (int i = n.length() - 1; i > 0; i--) {
            if (index[i] == k) {
                index[i] = 0;
                index[i - 1]++;
            }
        }
    }

    cout << answer;

    return 0;
}