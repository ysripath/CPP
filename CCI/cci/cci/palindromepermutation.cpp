#include <bits/stdc++.h>

using namespace std;


bool util(string str)
{
	std::transform(str.begin(), str.end(), str.begin(), ::tolower);
	set<char> s;
	for (auto x : str)
	{
		if (x == ' ')
			continue;
		auto itr = find(s.begin(), s.end(), x);
		if (itr == s.end())
		{
			s.insert(x);
		}
		else
		{
			s.erase(x);
		}
	}

	if (s.size() > 1)
		return false;
	else
		return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout << "Enter the test string\n";
	string str = "";
	char c;
	while (cin.get(c))
	{
		if (c == '\n')
			break;
		str += c;
	}

	if (util(str))
		cout << "Palindrom possible\n";
	else
		cout << "No palindrome permutation\n";
	return 0;	
}