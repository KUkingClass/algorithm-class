#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 2022 09 29 17 16
// 2022 09 29 18 00

int n, m, k, r, c;
vector<vector<int>> v;
vector<vector<int>> sticker;

bool isStickable(int x, int y) {
    if (x + r > n || y + c > m) {
        return false;
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (v[x + i][y + j] & sticker[i][j]) {
                return false;
            }
        }
    }

    return true;
}

void stick(int x, int y) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            v[x + i][y + j] |= sticker[i][j];
        }
    }
}

void rotate() {
    vector<vector<int>> newSticker(c, vector<int>(r, 0));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            newSticker[j][r - 1 - i] = sticker[i][j];
        }
    }
    newSticker.swap(sticker);
    swap(r, c);
}

int main() {
    // boj 18808

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    vector<vector<int>>(n, vector<int>(m, 0)).swap(v);

    while (k--) {
        cin >> r >> c;

        vector<vector<int>>(r, vector<int>(c, 0)).swap(sticker);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> sticker[i][j];
            }
        }

        bool flag = true;
        for (int d = 0; d < 360 && flag; d += 90) {
            if (d > 0) rotate();
            for (int i = 0; i < n && flag; i++) {
                for (int j = 0; j < m && flag; j++) {
                    if (isStickable(i, j)) {
                        stick(i, j);
                        flag = false;
                    }
                }
            }
        }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            answer += v[i][j];
        }
    }
    cout << answer;
    return 0;
}