#include <iostream>
#include <vector>

using namespace std;
// 2022 10 13 15 47
// 2022 10 13 16 48

vector<vector<int>> t;
int last_node = -1;

void traversal(int cur) {
    if (cur == -1) return;

    traversal(t[cur][1]);
    last_node = cur;
    traversal(t[cur][2]);
}

int main() {
    // boj 22856

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<vector<int>>(n + 1, vector<int>(4, 0)).swap(t);
    for (int i = 0; i < n; i++) {
        int num = 0;
        cin >> num;
        cin >> t[num][1] >> t[num][2];
        if (t[num][1] > 0) t[t[num][1]][3] = num;
        if (t[num][2] > 0) t[t[num][2]][3] = num;
    }
    
    traversal(1);
    
    int cur = 1;
    int answer = 0;

    while (true) {
        t[cur][0] = 1;

        if (t[cur][1] > 0 && t[t[cur][1]][0] != 1) { // 왼쪽 자식이 있는데 아직 방문 안 한 경우
            cur = t[cur][1];
        }
        else if (t[cur][2] > 0 && t[t[cur][2]][0] != 1) { // 오른쪽 자식이 있는데 아직 방문 안 한 경우
            cur = t[cur][2];
        }
        else if (cur == last_node) {
            break;
        }
        else {
            cur = t[cur][3];
        }
        answer++;
    }
    
    cout << answer;
    return 0;
}