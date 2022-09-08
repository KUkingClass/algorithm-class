#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
// 2022 09 07 23 44
// 2022 09 08 15 37

bool comp(vector<string> v1, vector<string> v2) {

    for (int i = 0; i < min(v1.size(), v2.size()); i++) {
        if (v1[i] != v2[i]) {
            if ('0' <= v1[i][0] && v1[i][0] <= '9' && '0' <= v2[i][0] && v2[i][0] <= '9') {
                int countZero1 = 0, countZero2 = 0;
                for (int j = 0; j < v1[i].length(); j++) {
                    if (v1[i][j] == '0') countZero1++;
                    else break;
                }
                for (int j = 0; j < v2[i].length(); j++) {
                    if (v2[i][j] == '0') countZero2++;
                    else break;
                }

                string s1 = v1[i].substr(countZero1, v1[i].length() - countZero1);
                string s2 = v2[i].substr(countZero2, v2[i].length() - countZero2);
               
                if (s1.length() == s2.length()) {
                    if (s1 == s2) {
                        return countZero1 < countZero2;
                    }
                    else return s1 < s2;
                }
                else return s1.length() < s2.length();
            }
            else if ('0' <= v1[i][0] && v1[i][0] <= '9') {
                return true;
            }
            else if ('0' <= v2[i][0] && v2[i][0] <= '9') {
                return false;
            }
            else {
                if ('A' <= v1[i][0] && v1[i][0] <= 'Z' && 'A' <= v2[i][0] && v2[i][0] <= 'Z') {
                    return v1[i] < v2[i];
                }
                else if ('A' <= v1[i][0] && v1[i][0] <= 'Z') {
                    if (v1[i][0] + 32 == v2[i][0]) return true;
                    return v1[i][0] + 32 <= v2[i][0];
                }
                else if ('A' <= v2[i][0] && v2[i][0] <= 'Z') {
                    if (v1[i][0] == v2[i][0] + 32) return false;
                    return v1[i][0] <= v2[i][0] + 32;
                }
                else {
                    return v1[i] < v2[i];
                }
            }
        }
    }
    return v1.size() < v2.size();
}

int main() {
    // boj 20210

    int n;
    cin >> n;

    vector<vector<string>> v;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        vector<string> temp;
        string unit = "";
        for (int j = 0; j < s.length(); j++) {
            if ('0' <= s[j] && s[j] <= '9') {
                unit += s[j];
            }
            else {
                if (unit.length() > 0) {
                    temp.push_back(unit);
                    unit = "";
                }
                unit += s[j];
                temp.push_back(unit);
                unit = "";
            }
        }
        if (unit.length() > 0) {
            temp.push_back(unit);
        }
        v.push_back(temp);
    }

    sort(v.begin(), v.end(), comp);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < v[i].size(); j++) {
            cout << v[i][j];
        }
        cout << '\n';
    }
    
    return 0;
}