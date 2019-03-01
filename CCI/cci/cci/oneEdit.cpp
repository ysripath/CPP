#include <bits/stdc++.h>


using namespace std;

bool util(string a, string b)
{
	if (abs((int)a.length() - (int)b.length()) > 1)
		return false;

	std::transform(a.begin(), a.end(), a.begin(), ::tolower);
	std::transform(b.begin(), b.end(), b.begin(), ::tolower);

	map<char, int> m;
	for (auto x : a)
	{
		auto itr = m.find(x);//std::find(m.begin(), m.end(), x);
		if (itr == m.end())
		{
			m.insert(std::pair<char, int>(x, 1));
		}
		else
			itr->second++;
	}

	for (auto x : b)
	{

		auto itr = m.find(x); //std::find(m.begin(), m.end(), x);
		if (itr == m.end())
		{
			m.insert(std::pair<char, int>(x, 1));
		}
		else
		{
			itr->second--;
			if (itr->second == 0)
				m.erase(itr);
		}
	}


	int count = 0;
	auto itr = m.begin();
	while (itr != m.end())
	{
		count += itr->second;
		itr++;
	}

	if (count > 2)
		return false;
	else
		return true;

}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout << "Enter two strings to check for one edit \n";
	string str1, str2;
	cin >> str1 >> str2;
	if (util(str1, str2))
		cout << "YES\n";
	else
		cout << "NO\n";
	return 0;
}