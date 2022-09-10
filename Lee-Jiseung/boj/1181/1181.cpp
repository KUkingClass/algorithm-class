#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>

using namespace std;

bool compare(string s1, string s2) {
	if (s1.size() == s2.size()) {
		return s1 < s2;
	}
	return s1.size() < s2.size();
}

int main() {
	int n;
	cin >> n;

	vector<string> v;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		v.push_back(s);
	}

	sort(v.begin(), v.end(), compare);

	string temp= "";
	for (int i = 0; i < n; i++) {
		if(temp != v[i]) cout << v[i] << '\n';
		temp = v[i];
	}
}