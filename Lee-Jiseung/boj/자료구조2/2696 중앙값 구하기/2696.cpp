#include <iostream>
#include <vector>
#include <queue>

using namespace std;
// 2022 09 26 17 34
// 2022 09 26 18 35


int main() {
    // boj 2696

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int m;
        cin >> m;
        cout << (m + 1) / 2 << '\n';

        int medium = 0;
        cin >> medium;

        vector<int> answer(1, medium);
        priority_queue<int, vector<int>, less<int>> left;
        priority_queue<int, vector<int>, greater<int>> right;
        for (int i = 2; i <= m; i++) {
            int temp;
            cin >> temp;

            if (temp < medium) 
                left.push(temp);
            else 
                right.push(temp);

            if (i % 2 == 1) {
                while (left.size() != right.size()) {
                    if (left.size() < right.size()) {
                        left.push(medium);
                        medium = right.top();
                        right.pop();
                    }
                    else {
                        right.push(medium);
                        medium = left.top();
                        left.pop();
                    }
                }
                
                answer.push_back(medium);
            }

            if (answer.size() == 10) {
                for (int j = 0; j < answer.size(); j++) 
                    cout << answer[j] << ' ';
                cout << '\n';
                vector<int>().swap(answer);
            }
        }
        for (int j = 0; j < answer.size(); j++) 
            cout << answer[j] << ' ';
        cout << '\n';
    }
    
    return 0;
}