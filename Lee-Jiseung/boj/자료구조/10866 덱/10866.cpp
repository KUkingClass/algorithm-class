#include <iostream>
#include <deque>

using namespace std;
// 2022 09 17 16 27
// 2022 09 17 16 30


int main() {
    // boj 10866

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    deque<int> q;
    while (n--)
    {
        string inst;
        cin >> inst;

        if (inst == "push_front") {
            int x;
            cin >> x;

            q.push_front(x);
        }
        else if (inst == "push_back") {
            int x;
            cin >> x;

            q.push_back(x);
        }
        else if (inst == "pop_front") {
            if (q.empty()) {
                cout << -1 << '\n';
            }
            else {
                cout << q.front() << '\n';
                q.pop_front();
            }
        }
        else if (inst == "pop_back") {
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
        else if (inst == "front") {
            if (q.empty()) {
                cout << -1 << '\n';
            }
            else {
                cout << q.front() << '\n';
            }
        }
        else if (inst == "back") {
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