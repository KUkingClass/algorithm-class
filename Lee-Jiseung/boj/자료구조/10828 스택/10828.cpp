#include <iostream>
#include <deque>

using namespace std;
// 2022 09 17 14 20
// 2022 09 17 14 22


int main() {
    // boj 10828

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    deque<int> q;
    while (n--)
    {
        string inst;
        cin >> inst;

        if (inst == "push") {
            int x;
            cin >> x;

            q.push_back(x);
        }
        else if (inst == "pop") {
            if (q.empty()) {
                cout << -1 << '\n';
            }
            else {
                cout << q.back() << '\n';
                q.pop_back();
            }
        }
        else if (inst == "size") {
            cout << q.size() << '\n';
        }
        else if (inst == "empty") {
            if (q.empty()) cout << 1 << '\n';
            else cout << 0 << '\n';
        }
        else if (inst == "top") {
            if (q.empty()) {
                cout << -1 << '\n';
            }
            else {
                cout << q.back() << '\n';
            }
        }
    }
    
    return 0;
}