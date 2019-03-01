#include <bits/stdc++.h>
using namespace std;


string shortestPalindrome(string s) {
	if (s.length() <= 1)
		return s;
	std::transform(s.begin(), s.end(), s.begin(), ::tolower);
	string rev = "";
	int l = s.length();
	for (int i = l - 1; i >= 0; i--)
	{
		rev += s[i];
	}
	cout << rev << "\n";
	// Compare with reverse string 
	// Keep moving the index of rev string until all characters match or end of rev is reached.

	int j = 0;
	int k = 0;
	int i = 0;
	while (j < l)
	{
		if (s[i] == rev[j])
		{
			i++;
			j++;
			continue;
		}
		else
		{
			k++;
			i = 0;
			j = k;
		}
	}

	string ret = "";
	for (int x = 0; x < k; x++)
		ret += rev[x];
	ret += s;
	return ret;

}

int main()
{
	cout << "Enter string\n";
	string str;
	cin >> str;
	cout << shortestPalindrome(str) << "\n";
}