#include <iostream>
#include <vector>
#include <queue>

using namespace std;
// 2022 09 26 18 39
// 2022 09 26 18 42


int main() {
    // boj 11279

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    priority_queue<int, vector<int>, less<int>> pq;
    while (n--) {
        int x;
        cin >> x;

        if (x > 0) 
            pq.push(x);
        else {
            if (pq.empty()) 
                cout << 0 << '\n';
            else {
                cout << pq.top() << '\n';
                pq.pop();
            }
        }
    }
    return 0;
}