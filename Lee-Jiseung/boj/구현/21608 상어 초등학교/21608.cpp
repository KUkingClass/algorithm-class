#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 2022 10 12 18 51
// 2022 10 12 20 26

vector<vector<int>> v; // 자리
vector<vector<int>> num_empty; // 각 자리별 인접한 비어있는 칸의 수
vector<pair<int, int>> locs; // 학생별 자리 좌표
vector<vector<int>> p; // 선호하는 학생
vector<int> dr = { -1, 0, 1, 0 };
vector<int> dc = { 0, -1, 0, 1 };

bool comp(vector<int> v1, vector<int> v2) {
    if (v1[2] == v2[2]) {
        if (v1[3] == v2[3]) {
            return v1[0] * 100 + v1[1] < v2[0] * 100 + v2[1]; // 왼쪽 위
        }
        return v1[3] > v2[3]; // 비어있는 칸의 수
    }
    return v1[2] > v2[2]; // 선호하는 학생
}

int main() {
    // boj 21608

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<vector<int>>(n, vector<int>(n, 0)).swap(v);
    vector<pair<int, int>>(n * n + 1, { -1, -1 }).swap(locs);
    vector<vector<int>>(n, vector<int>(n, 4)).swap(num_empty);
    for (int i = 0; i < n; i++) { // 가장자리 비어있는 칸의 수 감소
        num_empty[0][i]--;
        num_empty[n - 1][i]--;
        num_empty[i][0]--;
        num_empty[i][n - 1]--;
    }

    int num, temp;
    vector<vector<int>>(n * n + 1, vector<int>(n * n + 1, 0)).swap(p);

    for (int t = 0; t < n * n; t++) {
        cin >> num;

        vector<vector<int>> infos; // 행, 열, 인접한 선호하는 학생 수, 인접한 비어있는 칸의 수
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                infos.push_back({ i, j, 0, num_empty[i][j] });
            }
        }

        for (int i = 0; i < 4; i++) {
            cin >> temp;
            p[num][temp] = 1;

            if (locs[temp].first < 0) continue;

            int x = locs[temp].first;
            int y = locs[temp].second;
            for (int j = 0; j < 4; j++) {
                if (x + dr[j] < 0 || x + dr[j] >= n || y + dc[j] < 0 || y + dc[j] >= n) {
                    continue;
                }
                infos[(x + dr[j]) * n + (y + dc[j])][2]++;
            }
        }

        sort(infos.begin(), infos.end(), comp);

        for (int i = 0; i < infos.size(); i++) {
            int x = infos[i][0];
            int y = infos[i][1];

            if (v[x][y] > 0) continue;
            locs[num] = { x, y };
            v[x][y] = num; // 자리 배정

            for (int j = 0; j < 4; j++) { // 배정한 자리의 인접한 자리의 인접한 비어있는 칸의 수 감소 
                if (x + dr[j] < 0 || x + dr[j] >= n || y + dc[j] < 0 || y + dc[j] >= n) {
                    continue;
                }
                num_empty[x + dr[j]][y + dc[j]]--;
            }
            break;
        }
    }

    int answer = 0;
    vector<int> score = { 0, 1, 10, 100, 1000 };
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int count = 0;
            for (int k = 0; k < 4; k++) {
                if (i + dr[k] >= 0 && i + dr[k] < n && j + dc[k] >= 0 && j + dc[k] < n) {
                    count += p[v[i][j]][v[i + dr[k]][j + dc[k]]];
                }
            }
            answer += score[count];
        }
    }
    cout << answer;
    return 0;
}