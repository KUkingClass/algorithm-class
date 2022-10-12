#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 2022 10 11 16 18
// 2022 10 11 21 16


int main() {
    // boj 21611

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    // 입력 저장
    vector<vector<int>> v(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> v[i][j];
        }
    }

    vector<int> change_directions = { 3, 2, 0, 1 };    // 벽에 부딪히면 바꿀 방향
    vector<int> dr = { -1, 1, 0, 0 };                   // 상하좌우
    vector<int> dc = { 0, 0, -1, 1 };

    vector<int> balls; // 상어의 위치부터 구슬의 번호를 1차원 벡터에 저장
    vector<vector<int>> locs(n, vector<int>(n, 0)); // 2차원 벡터 격자에 각 구슬의 1차원 벡터에서의 index 저장

    int x = 0, y = 0, d = 3, loc = n * n - 1;
    while (true) {
        locs[x][y] = --loc; // 해당 위치의 index 저장
        if (v[x][y] > 0) { // 구슬의 번호 저장
            balls.push_back(v[x][y]);
        }

        int newx = x + dr[d]; // 새로운 좌표
        int newy = y + dc[d];
        if (newx < 0 || newx >= n || newy < 0 || newy >= n || locs[newx][newy] > 0) { // 벽에 닿으면(격자를 빠져나가거나 방문했던 위치 방문) 방향 전환
            d = change_directions[d];
            newx = x + dr[d];
            newy = y + dc[d];
        }

        if (newx == n / 2 && newy == n / 2) { // 상어까지 가면 끝
            break;
        }
        
        x = newx;
        y = newy;
    }
    reverse(balls.begin(), balls.end()); // 1차원 벡터에 구슬을 뒤에서부터 넣었으니까 뒤집기

    int di, si;
    vector<int> count(4, 0); // 점수 저장
    while (m--) {
        cin >> di >> si;
        for (int i = 0; i < si; i++) { // 구슬 파괴하기
            int loc = locs[n / 2 + (i + 1) * dr[di - 1]][n / 2 + (i + 1) * dc[di - 1]] - i; // 파괴할 구슬의 위치
            if (loc >= balls.size()) break; // 파괴할 위치에 구슬 없으면 그만
            balls.erase(balls.begin() + loc);
        }

        bool flag = true;
        int num = -1;  // 이전 구슬의 번호
        int num_count = -1; // 이전 구슬의 번호가 연속된 개수
        while (flag) { // 폭발하지 않을 때까지 반복
            flag = false;
            num = -1;
            num_count = -1;
            for (int i = 0; i < balls.size(); i++) {
                if (balls[i] == num) {
                    num_count++;
                }
                else {
                    if (num_count >= 4) {
                        balls.erase(balls.begin() + i - num_count, balls.begin() + i); // 연속된 개수만큼 삭제
                        i -= num_count; // 삭제한만큼 인덱스 감소
                        count[num] += num_count; // 점수 반영
                        flag = true;
                    }
                    num = balls[i];
                    num_count = 1;
                }
            }
            if (num_count >= 4) {
                balls.erase(balls.end() - num_count, balls.end()); // 연속된 개수만큼 삭제
                count[num] += num_count; // 점수 반영
                flag = true;
            }
        }
        
        if (balls.empty()) break;
        num = balls[0]; // 이전 구슬의 번호
        num_count = 1; // 이전 구슬의 번호가 연속된 개수
        for (int i = 1; i < balls.size(); i++) {
            if (balls[i] == num) {
                num_count++;
            }
            else {
                balls.erase(balls.begin() + i - num_count, balls.begin() + i); // 연속된 개수만큼 삭제
                i -= num_count; // 삭제한만큼 인덱스 감소
                balls.emplace(balls.begin() + i++, num_count);
                balls.emplace(balls.begin() + i++, num);
                num = balls[i];
                num_count = 1;
            }
        }
        balls.erase(balls.end() - num_count, balls.end()); // 연속된 개수만큼 삭제
        balls.emplace_back(num_count);
        balls.emplace_back(num);
        if (balls.size() > n * n - 1) { // 너무 길면 자르기
            balls = { balls.begin(), balls.begin() + n*n-1 };
        }
    }

    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += i * count[i];
    }
    cout << sum;
    return 0;
}