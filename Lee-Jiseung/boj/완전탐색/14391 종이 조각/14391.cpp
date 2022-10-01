#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 2022 09 29 20 28
// 2022 09 30 20 30

int n, m;
int answer = -1;
vector<vector<int>> v;
vector<vector<int>> nums;

void calculate() {
    int sum = 0;
    vector<vector<int>> visited = { nums.begin(), nums.end() };

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j] >= 0) {
                int count = visited[i][j];
                visited[i][j] = -1;
                int temp = v[i][j];

                int k = 1;
                while (j + k < m && count == visited[i][j + k]) {
                    temp = temp * 10 + v[i][j + k];
                    visited[i][j + k] = -1;
                    k++;
                }

                k = 1;
                while (i + k < n && count == visited[i + k][j]) {
                    temp = temp * 10 + v[i + k][j];
                    visited[i + k][j] = -1;
                    k++;
                }

                sum += temp;
            }
        }
    }

    answer = max(sum, answer);
}

void numbering(int count) {
    int x = -1, y = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (nums[i][j] < 0) {
                x = i;
                y = j;
                break;
            }
        }
        if (x + y >= 0) break;
    }
    if (x + y < 0) {
        calculate();
        return;
    }

    int i = x;
    for (; i < n; i++) {
        if (nums[i][y] >= 0) {
            break;
        }
        nums[i][y] = count;
        numbering(count + 1);
    }
    for (i--; i > x; i--) {
        nums[i][y] = -1;
    }
    i = y + 1;
    for (; i < m; i++) {
        if (nums[x][i] >= 0) {
            break;
        }
        nums[x][i] = count;
        numbering(count + 1);
    }
    for (i--; i >= y; i--) {
        nums[x][i] = -1;
    }
}

int main() {
    // boj 14391

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;
    vector<vector<int>>(n, vector<int>(m, 0)).swap(v);
    vector<vector<int>>(n, vector<int>(m, -1)).swap(nums);

    for (int i = 0; i < n; i++) {
        string temp;
        cin >> temp;
        for (int j = 0; j < m; j++) {
            v[i][j] = temp[j] - '0';
        }
    }

    numbering(0);
    
    cout << answer;
    return 0;
}