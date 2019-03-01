#include <bits/stdc++.h>

using namespace std;
typedef std::function<bool(std::pair<char, int>, std::pair<char, int>)> Comparator;
string frequencySort(string s) {

	if (s.length() <= 2)
		return s;

	std::transform(s.begin(), s.end(), s.begin(), ::tolower);
	//cout << s << endl;
	map<char, int> m;

	for (auto x : s)
	{
		auto itr = m.find(x);
		if (itr == m.end()) {
			//cout << x << "\n";
			m.insert(std::pair<char, int>(x, 1));
		}
		else
			itr->second++;
	}
	Comparator compFunctor =
		[](std::pair<char, int> elem1, std::pair<char, int> elem2)
	{
		//cout << elem1.first << "----" << elem2.first << endl;
		return elem1.second > elem2.second;
	};

	std::vector<pair<char, int>> v;
	auto itr = m.begin();
	while (itr != m.end())
	{
		v.emplace_back(pair<char, int>(itr->first, itr->second));
		itr++;
	}
	std::sort(v.begin(), v.end(), compFunctor);
	string ret = "";
	auto itr1 = v.begin();
	while (itr1 != v.end())
	{
		//cout << itr1->first << "\n";
		for (int i = 0; i < itr1->second; i++)
			ret += itr1->first;
		itr1++;
	}	

	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cout << "Enter string\n";
	string str;
	cin >> str;
	cout << frequencySort(str) << "\n";

}