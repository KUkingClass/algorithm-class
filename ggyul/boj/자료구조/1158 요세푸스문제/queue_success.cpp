// https://www.acmicpc.net/problem/1158
// 요세푸스 문제
#include <iostream>
#include <queue>
#include <vector>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    queue<int> q;
    vector<int> result;
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }
    while (!q.empty()) {
        for (int i = 0; i < k - 1; i++) {
            int next = q.front();
            q.pop();
            q.push(next);
        }
        result.push_back(q.front());
        q.pop();
    }

    cout << "<";
    for (int i = 0; i < result.size() - 1; i++) {
        cout << result[i] << ", ";
    }

    cout << result[result.size() - 1] << ">";
    return 0;
}
