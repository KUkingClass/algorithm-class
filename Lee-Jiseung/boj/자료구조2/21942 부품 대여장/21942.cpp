#include <iostream>
#include <vector>
#include <map>

using namespace std;
// 2022 09 26 15 17
// 2022 09 26 17 21


int main() {
    // boj 21942

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long f;
    string l;
    cin >> n >> l >> f;

    vector<int> v = { 24 * 60 * 100,24 * 60 * 10,24 * 60,0,60 * 10,60,0,10,1 };
    int due = 0;
    for (int i = 0; i < l.length(); i++)
        due += (l[i] - '0') * v[i];

    vector<int> dates = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    map<pair<string, string>, int> m;
    map<string, long long> fees;
    while (n--) {
        string ymd, hm, pname, uname;
        cin >> ymd >> hm >> pname >> uname;

        int month = (ymd[5] - '0') * 10 + (ymd[6] - '0');
        int date = (ymd[8] - '0') * 10 + (ymd[9] - '0');
        for (int i = 0; i < month; i++)
            date += dates[i];
        int minute = (hm[3] - '0') * 10 + (hm[4] - '0') + ((hm[0] - '0') * 10 + (hm[1] - '0')) * 60;

        int time = date * 60 * 24 + minute;
        
        pair<string, string> p = { uname, pname };
        if (m.find(p) != m.end()) {
            int duetime = m[p] + due;
            if (duetime < time)
                if (fees.find(uname) != fees.end())
                    fees[uname] += ((long long) time - duetime) * f;
                else
                    fees[uname] = ((long long) time - duetime) * f;
            m.erase(p);
        }
        else
            m[p] = time;
    }

    if (fees.empty())
        cout << -1;
    else
        for (auto iter = fees.begin(); iter != fees.end(); iter++)
            cout << iter->first << ' ' << iter->second << '\n';

    return 0;
}